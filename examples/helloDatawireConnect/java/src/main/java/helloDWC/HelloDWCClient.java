package helloDWC;

import quark.concurrent.FutureWait;
import hello.HelloClient;
import hello.Request;
import hello.Response;

import datawire_connect.resolver.DiscoveryConsumer;
import datawire_discovery.client.GatewayOptions;

public class HelloDWCClient {
    // What's with the InterruptedException? We use Thread.sleep below, and
    // Thread.sleep can throw InterruptedException. We don't want to bother 
    // catching it for this example, since it shouldn't ever happen in our
    // situation, and if it does, well, there's nothing much we should do 
    // except rethrow anyway...

    public static void main(String[] args) throws InterruptedException {
        HelloClient client = new HelloClient("hello");

        GatewayOptions options =
            new GatewayOptions("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOnsiZHc6c2VydmljZTAiOnRydWV9LCJvd25lckVtYWlsIjoiZmx5bm5AZGF0YXdpcmUuaW8iLCJkd1R5cGUiOiJEYXRhV2lyZUNyZWRlbnRpYWwiLCJuYmYiOjE0NTg3NjI5NDIsInN1YiI6ImhlbGxvIiwiYXVkIjoiQUROUDgwMUFHNCIsImlzcyI6ImNsb3VkLWh1Yi5kYXRhd2lyZS5pbyIsImp0aSI6IjUxZjA0ZGNiLTY1YWQtNDM3NS05OGFhLTcxMWI4OWRlOGU0OCIsImV4cCI6MTQ1OTk3MjU0MiwiaWF0IjoxNDU4NzYyOTQyLCJlbWFpbCI6bnVsbH0.b6WKhD86E45bxSPVdbRQzkEEJQpZ0bQwmi-jRitwtlE");

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
