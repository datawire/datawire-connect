package helloDWC;

import hello.HelloServer;
import datawire_connect.resolver.DiscoveryProvider;
import datawire_discovery.model.Endpoint;
import datawire_discovery.client.GatewayOptions;

public class HelloDWCServer {

    public static void main(String[] args) {
        String url = "http://127.0.0.1:8910/";

        HelloImpl impl = new HelloImpl();
        HelloServer server = new HelloServer(impl);
        server.serveHTTP(url);

        Endpoint endpoint = 
            new Endpoint("http", "127.0.0.1", 8910, url);

        GatewayOptions options =
            new GatewayOptions("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzY29wZXMiOnsiZHc6c2VydmljZTAiOnRydWV9LCJvd25lckVtYWlsIjoiZmx5bm5AZGF0YXdpcmUuaW8iLCJkd1R5cGUiOiJEYXRhV2lyZUNyZWRlbnRpYWwiLCJuYmYiOjE0NTg3NjI5NDIsInN1YiI6ImhlbGxvIiwiYXVkIjoiQUROUDgwMUFHNCIsImlzcyI6ImNsb3VkLWh1Yi5kYXRhd2lyZS5pbyIsImp0aSI6IjUxZjA0ZGNiLTY1YWQtNDM3NS05OGFhLTcxMWI4OWRlOGU0OCIsImV4cCI6MTQ1OTk3MjU0MiwiaWF0IjoxNDU4NzYyOTQyLCJlbWFpbCI6bnVsbH0.b6WKhD86E45bxSPVdbRQzkEEJQpZ0bQwmi-jRitwtlE");

        DiscoveryProvider provider =
            new DiscoveryProvider(options, "hello", endpoint);

        provider.register(15.0);
    }
}
