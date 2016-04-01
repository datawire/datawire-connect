package helloDWC;

import quark.concurrent.FutureWait;
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
        DatawireState dwState = DatawireState.defaultState();
        String token = dwState.getCurrentServiceToken("hello");

        HelloClient client = new HelloClient("hello");

        GatewayOptions options = new GatewayOptions(token);

        DiscoveryConsumer resolver = new DiscoveryConsumer(options);

        client.setResolver(resolver);

        // Give the resolver a chance to get connected....
        Thread.sleep(5000);

        Request request = new Request();

        if (args.length > 0) {
            request.text = args[0];
        } else {
            request.text = "Hello from Java!";
        }

        System.out.println("Request says: " + request.text);

        Response response = client.hello(request);
        response.await(1.0);

        // Since we didn't wait indefinitely, we might've gotten a timeout.
        // Therefore, we need to start by checking response.isFinished().

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
