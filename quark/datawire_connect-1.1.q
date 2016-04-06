package datawire_connect 1.1.0;

// We rely on the Discovery Service.
use https://raw.githubusercontent.com/datawire/discovery/master/quark/discovery-1.0.0.q;

import datawire_discovery;

include _datawire_fs_impl.py;
include _datawire_fs_impl.js;
include io/datawire/quark/_datawire_fs_impl.java;

// WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING
//
// DO NOT RELY ON THE NAME _datawire_fs TOO MUCH. IT IS ABOUT TO MOVE
// INTO QUARK ITSELF.
//
// WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING

namespace _datawire_fs {
  macro String dwfs_userHomeDir()
    $py{__import__('_datawire_fs_impl')._datawire_fs.userHomeDir()}
    $js{require('datawire_connect/_datawire_fs_impl.js').userHomeDir()}
    $java{io.datawire.quark.runtime._datawire_fs_impl.userHomeDir()};

  macro String dwfs_fileContents(String path)
    $py{__import__('_datawire_fs_impl')._datawire_fs.fileContents($path)}
    $js{require('datawire_connect/_datawire_fs_impl.js').fileContents($path)}
    $java{io.datawire.quark.runtime._datawire_fs_impl.fileContents($path)};

  class FS {
    static String userHomeDir() {
      return dwfs_userHomeDir();
    }

    static String fileContents(String path) {
      return dwfs_fileContents(path);
    }        
  }
}

namespace datawire_connect {

  namespace state {
    class DatawireState {
      bool _initialized;
      Runtime runtime;

      JSONObject object;
      JSONObject orgs;

      /*
       * _defaultOrg reflects the 'orgID' element saved in the state
       * dictionary itself.
       *
       * _currentOrg reflects the org named by the 'switchToOrg' method.
       *
       * The two start out the same, but the current org can be switched.
       */

      String _defaultOrgID;
      JSONObject _defaultOrg;

      String _currentOrgID;
      JSONObject _currentOrg;

      @doc("DatawireState.defaultState() is the normal entry point.")
      static DatawireState defaultState() {
        DatawireState dwState = new DatawireState();

        dwState.loadDefaultState();

        return dwState;
      }

      @doc("DatawireState.customState() is the normal entry point if you're using a custom state file")
      static DatawireState customState(String path) {
        DatawireState dwState = new DatawireState();

        dwState.load(path);

        return dwState;
      }

      DatawireState() {
        self._initialized = false;
        self.runtime = concurrent.Context.runtime();
      }

      void load(String jsonInput) {
        JSONObject obj = jsonInput.parseJSON();

        if (!obj.isDefined()) {
          self.runtime.fail("DatawireState: Invalid JSON, cannot load");
        }

        JSONObject orgs = obj["orgs"];

        if (!orgs.isDefined()) {
          self.runtime.fail("DatawireState: no orgs present in input JSON!");
        }

        self.object = obj;
        self.orgs = orgs;

        obj = self.object["orgID"];

        if (!obj.isDefined()) {
          self.runtime.fail("DatawireState: no default org ID present in input JSON!");
        }

        if (!obj.isString()) {
          self.runtime.fail("DatawireState: default org ID in input JSON is not a string!");
        }

        self._defaultOrgID = obj.getString();

        obj = self.orgs[self._defaultOrgID];

        if (!obj.isDefined()) {
          self.runtime.fail("DatawireState: default org ID in input JSON is invalid!");
        }

        self._defaultOrg = obj;

        // Do switchToOrg by hand, since we're not initialized yet.
        self._currentOrgID = self._defaultOrgID;
        self._currentOrg = self._defaultOrg;

        self._initialized = true;
      }

      void switchToOrg(String orgID) {
        // If you add anything here, you'll need to revist the "Do switchToOrg by hand"
        // comment above.

        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        JSONObject org = self.orgs[orgID];

        if (!org.isDefined()) {
          self.runtime.fail("DatawireState: org " + orgID + " is not valid");
        }

        self._currentOrgID = orgID;
        self._currentOrg = org;
      }

      String getDefaultOrgID() {
        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        return self._defaultOrgID;
      }

      JSONObject getDefaultOrg() {
        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        return self._defaultOrg;
      }

      String getCurrentOrgID() {
        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        return self._currentOrgID;
      }

      JSONObject getCurrentOrg() {
        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        return self._currentOrg;
      }

      String getCurrentEmail() {
        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        return self._currentOrg["email"].getString();
      }

      List<String> getCurrentServices() {
        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        return self._currentOrg["service_tokens"].keys();
      }

      String getCurrentServiceToken(String service_handle) {
        if (!self._initialized) {
          self.runtime.fail("DatawireState: call load() before attempting any operations");
        }

        return self._currentOrg["service_tokens"][service_handle].getString();
      }

      String stateContents(String path) {
        return _datawire_fs.FS.fileContents(path);
      }

      String defaultStatePath() {
        return _datawire_fs.FS.userHomeDir() + "/.datawire/datawire.json";
      }

      String defaultStateContents() {
        return self.stateContents(self.defaultStatePath());
      }

      void loadDefaultState() {
        self.load(self.defaultStateContents());
      }
    }
  }

  namespace resolver {
    class DiscoClient extends client.CloudDiscoveryClient {
      BaseDiscoResolver resolver;

      DiscoClient(BaseDiscoResolver resolver, client.GatewayOptions gateway, String serviceName, model.Endpoint endpoint) {
        super(concurrent.Context.runtime(), gateway, serviceName, endpoint);
        self.resolver = resolver;
      }

      void onConnected(event.Connected connected) {
        self.resolver.onConnected(connected);
      }

      void onSubscribed(message.Subscribe subscribed) {
        self.resolver.onSubscribed(subscribed);
      }
    }


    @doc("BaseDiscoResolver has the basic logic to use the Discovery service to resolve names into URLs.")
    class BaseDiscoResolver extends Resolver {
      static Logger logger = new Logger("DWC");

      DiscoClient disco;

      List<String> resolve(String serviceName) {
        logger.debug("DWC resolving " + serviceName);

        List<model.Endpoint> endpoints = self.disco.getRoutes(serviceName);

        // String allURLs = "";
        List<String> urls = [];

        int i = 0;

        while (i < endpoints.size()) {
          urls.add(endpoints[i].uri);
          // allURLs = allURLs + " " + endpoints[i].uri;
          i = i + 1;        
        }

        logger.debug("DWC resolved " + serviceName + " => " +  urls.toString());

        return urls;
      }

      void onConnected(event.Connected connected) {}
      void onSubscribed(message.Subscribe subscribed) {}
    }

    @doc("DiscoveryConsumer uses Datawire Connect's Discovery service to resolve service names to URLs, but doesn't provide any services itself.")
    class DiscoveryConsumer extends BaseDiscoResolver {
      DiscoveryConsumer(client.GatewayOptions options) {
        self.disco = new DiscoClient(self, options, null, null);

        self.disco.connect();
      }

      void onConnected(event.Connected connected) {
        self.disco.subscribe();
      }

      void onSubscribed(message.Subscribe subscribed) {
        self.disco.logger.info("SUBSCRIBED");
      }
    }

    class AutoHeartbeat extends Task {
      DiscoveryProvider provider;
      float interval;

      AutoHeartbeat(DiscoveryProvider provider, float interval) {
        self.provider = provider;
        self.interval = interval;

        self.reschedule(concurrent.Context.runtime());
      }

      void reschedule(Runtime runtime) {
        runtime.schedule(self, self.interval);
      }

      void onExecute(Runtime runtime) {
        self.provider.disco.logger.info("heartbeat! for " + self.provider.disco.endpoint.toString());

        // XXX BRUTAL HACK HERE XXX
        // We should be calling self.provider.disco.heartbeat() here, but that doesn't actually
        // keep our route from expiring right now, so for the moment we'll just re-call 
        // registerEndpoint.

        // self.provider.disco.heartbeat();       // XXX see above!
        self.provider.disco.registerEndpoint();

        self.reschedule(runtime);
      }
    }

    @doc("DiscoveryProvider uses Datawire Connect's Discovery service to register a service-to-URL mapping, and to resolve other service names to URLs")
    class DiscoveryProvider extends BaseDiscoResolver {
      AutoHeartbeat pulse;
      float heartbeatInterval;

      DiscoveryProvider(client.GatewayOptions options, String serviceName, model.Endpoint endpoint) {
        self.disco = new DiscoClient(self, options, serviceName, endpoint);
        self.heartbeatInterval = 0.0;
      }

      void register(float heartbeatInterval) {
        self.heartbeatInterval = heartbeatInterval;

        self.disco.connect();
      }

      void onConnected(event.Connected connected) {
        self.disco.registerEndpoint();

        if (self.heartbeatInterval > 0.0) {
          self.pulse = AutoHeartbeat(self, self.heartbeatInterval);
        }
      }

      void onSubscribed(message.Subscribe subscribed) {
        self.disco.logger.info("SUBSCRIBED");
      }
    }
  }
}
