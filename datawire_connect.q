// We rely on the Discovery Service.
use https://raw.githubusercontent.com/datawire/discovery/flynn/feature/discoball/discovery.q;
// use file:///Users/flynn/datawire/discovery/discovery.q;

import discovery;

namespace datawire_connect {
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
