package helloDWC;

import hello.HelloClient;
import hello.Request;
import hello.Response;

import datawire_connect.resolver.DiscoveryConsumer;
import datawire_connect.state.DatawireState;
import datawire_discovery.client.GatewayOptions;

public class HelloDWCClient {
    // What's with the InterruptedException? We use Thread.sleep below, and
    // Thread.sleep can throw InterruptedException. We don't want to bother 
    // catching it for this example, since it shouldn't ever happen in our
    // situation, and if it does, well, there's nothing much we should do 
    // except rethrow anyway...

    public static void main(String[] args) throws InterruptedException {
        String text = "Hello from Java!";

        if (args.length > 0) {
            text = args[0];
        }

        // Grab our service token.
        DatawireState dwState = DatawireState.defaultState();
        String token = dwState.getCurrentServiceToken("hello");

        // Set up the client...
        HelloClient client = new HelloClient("hello");

        // ...and tell it that we want to use Datawire Connect to find
        // providers of this service.
        GatewayOptions options = new GatewayOptions(token);
        DiscoveryConsumer resolver = new DiscoveryConsumer(options);

        client.setResolver(resolver);

        // Give the resolver a chance to get connected.
        Thread.sleep(5000);

        // OK, make the call!
        Request request = new Request();
        request.text = text;

        System.out.println("Request says: " + request.text);

        Response response = client.hello(request);
        response.await(1.0);

        if (!response.isFinished()) {
            System.out.println("No response!");
        }
        else if (response.getError() != null) {
            System.out.println("Response failed with: " + response.getError());
        }
        else {
            System.out.println("Response says: " + response.result);
        }
    }
}
