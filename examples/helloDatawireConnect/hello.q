package hello 1.0.0;

// We'll be using Datawire Connect for this...
use https://raw.githubusercontent.com/datawire/datawire-connect/flynn/feature/version1.1/quark/datawire_connect-1.1.q;

// ...and we need to worry about concurrency, too.
import quark.concurrent;

// In your target language, the thing you'll pull into your code will
// be called "hello".
namespace hello {
    @doc("A value class for Request data for the hello service.")
    class Request {
        String text;
    }

    // Response (below) extends Future so that our RPC calls can
    // return immediately, rather than always having to block for 
    // the RPC to finish. Be sure you wait for the Response object
    // to be marked finished before trying to look at the results!

    @doc("A value class for Response data from the hello service.")
    class Response extends Future {
        @doc("A greeting from the hello service.")
        String result;
    }

    @doc("The hello service.")
    interface Hello extends Service {
    	// How long (in seconds) the remote request is given to complete
        static float timeout = 3.0;

    	// Number of failed requests before circuit breaker trips
        static int failureLimit = 1;

    	// How long (in seconds) before circuit breaker resets
        static float retestDelay = 30.0;

        @doc("Respond to a hello request.")
        Response hello(Request request) {
    	    // The ? operator casts the return value to whatever type is
            // needed -- so here, it means "cast to Response".
            return ?self.rpc("hello", [request]);
        }
    }

    @doc("A client adapter for the hello service.")
    class HelloClient extends Client, Hello {}

    @doc("A server adapter for the hello service.")
    class HelloServer extends Server<Hello> {}
}
