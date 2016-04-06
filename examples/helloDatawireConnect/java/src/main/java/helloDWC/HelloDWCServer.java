package helloDWC;

import hello.HelloServer;

import datawire_connect.resolver.DiscoveryProvider;
import datawire_connect.state.DatawireState;
import datawire_discovery.model.Endpoint;
import datawire_discovery.client.GatewayOptions;

/******** MAINLINE ********/
// (service implementation is in HelloDWCImpl.java)

public class HelloDWCServer {

    public static void main(String[] args) {
        // Grab our service token.
        DatawireState dwState = DatawireState.defaultState();
        String token = dwState.getCurrentServiceToken("hello");

        System.out.println("off we go");

        // Start our server running...
        String url = "http://127.0.0.1:8910/";

        HelloImpl impl = new HelloImpl();
        HelloServer server = new HelloServer(impl);
        server.sendCORS(true);
        server.serveHTTP(url);

        // ...and then register it with Datawire Connect.
        Endpoint endpoint = 
            new Endpoint("http", "127.0.0.1", 8910, url);

        GatewayOptions options = new GatewayOptions(token);

        DiscoveryProvider provider =
            new DiscoveryProvider(options, "hello", endpoint);

        provider.register(15.0);

        System.out.println("registered Java server on " + url);
    }
}
