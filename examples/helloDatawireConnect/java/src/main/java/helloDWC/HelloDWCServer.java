package helloDWC;

import hello.HelloServer;

import datawire_connect.resolver.DiscoveryProvider;
import datawire_connect.state.DatawireState;
import datawire_discovery.model.Endpoint;
import datawire_discovery.client.GatewayOptions;

public class HelloDWCServer {

    public static void main(String[] args) {
        String url = "http://127.0.0.1:8910/";

        DatawireState dwState = DatawireState.defaultState();
        String token = dwState.getCurrentServiceToken("hello");

        HelloImpl impl = new HelloImpl();
        HelloServer server = new HelloServer(impl);
        server.serveHTTP(url);

        Endpoint endpoint = 
            new Endpoint("http", "127.0.0.1", 8910, url);

        GatewayOptions options = new GatewayOptions(token);

        DiscoveryProvider provider =
            new DiscoveryProvider(options, "hello", endpoint);

        provider.register(15.0);
    }
}
