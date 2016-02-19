// We rely on the Discovery Service.
use https://raw.githubusercontent.com/datawire/discovery/master/discovery.q;
import discovery;

namespace datawire_connect {
  namespace resolver {
    @doc("BaseDiscoResolver has the basic logic to use the Discovery service to resolve names into URLs.")
    class BaseDiscoResolver extends Resolver {
      client.DiscoveryClient disco;

      List<String> resolve(String serviceName) {
        List<model.Endpoint> endpoints = self.disco.getRoutes(serviceName);

        List<String> urls = [];

        int i = 0;

        while (i < endpoints.size()) {
          urls.add(endpoints[i].uri);
          i = i + 1;        
        }

        return urls;
      }
    }

    @doc("DiscoveryConsumer uses Datawire Connect's Discovery service to resolve service names to URLs, but doesn't provide any services itself.")
    class DiscoveryConsumer extends BaseDiscoResolver {
      DiscoveryConsumer(client.GatewayOptions options) {
        self.disco = new client.CloudDiscoveryClient(concurrent.Context.runtime(), options, null, null);
      }
    }

    @doc("DiscoveryProvider uses Datawire Connect's Discovery service to register a service-to-URL mapping, and to resolve other service names to URLs")
    class DiscoveryProvider extends BaseDiscoResolver {
      DiscoveryProvider(client.GatewayOptions options, String serviceName, model.Endpoint endpoint) {
        self.disco = new client.CloudDiscoveryClient(concurrent.Context.runtime(), options, serviceName, endpoint);
      }
    }
  }
}