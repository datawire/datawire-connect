package helloDWC;

import hello.Hello;
import hello.Request;
import hello.Response;

/******** SERVICE IMPLEMENTATION ********/
// (mainline is in HelloDWCServer.java)

public class HelloImpl extends quark.BaseService implements Hello {

    @Override
    public Response hello(Request request) {
        // Say hello!

        // Snare a response object...
        Response response = new Response();

        // ...and fill it in.
        response.result = "Responding to [" + request.text + "] from Java";

        // Uncomment this try block to simulate a long request processing
        // time (which may cause a timeout for the client, of course).
        // try {
        //   Thread.sleep(5000);
        // }
        // catch(InterruptedException ex) {
        // }

        // Mark our response as finished, so that when our caller gets
        // it, they know that everything that needs doing is done.
        response.finish(null);

        return response;
    }

}
