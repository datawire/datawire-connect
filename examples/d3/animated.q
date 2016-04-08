package animated 1.0.0;

use https://raw.githubusercontent.com/datawire/datawire-connect/develop/quark/datawire_connect-1.1.q;

import quark.concurrent;

namespace animated {

    @doc("A value class for Request data for the animated service.")
    class Request {
        int color;
        int octet;
    }

    @doc("A value class for Response data from the animated service.")
    // The RPC call immediately returns a Future object
    // that can be processed by a listener
    class Response extends Future {
        @doc("A response from the animated service.")
        int color;
        int instance;
    }

    @doc("The animated service.")
    interface Animated extends Service {
    	// How long (in seconds) the remote request is given to complete
        static float timeout = 3.0;
    	// Number of failed requests before circuit breaker trips
        static int failureLimit = 1;
    	// How long (in seconds) before circuit breaker resets
        static float retestDelay = 30.0;

        @doc("Respond to a animated request.")
        Response animated(Request request) {
    	    // ? operator casts the return value to a Response object
            return ?self.rpc("animated", [request]);
        }
    }

    @doc("A client adapter for the animated service.")
    class AnimatedClient extends Client, Animated {}

    @doc("A server adapter for the animated service.")
    class AnimatedServer extends Server<Animated> {}

}
