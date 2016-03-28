package ratings 0.0.1;

use ../../../quark/datawire_connect-1.0.0.q;

import datawire_connect.resolver;
import builtin.concurrent;

namespace ratings {
  // Rating is the data structure we'll be passing around between the microservice
  // and its client. It extends Future because the RPC can take awhile, and we don't
  // want to block in the process.

  class Rating extends Future {
    String thingID;  // We include the thingID with its rating just to make it a
    int rating;    // little easier to keep track of what's what.
  }

  // RatingsResolver is test resolver for use with localhost.

  class RatingsResolver extends Resolver {
    List<String> resolve(String serviceName) {
      return [ "http://127.0.0.1:8001/" + serviceName,
               "http://127.0.0.1:8002/" + serviceName, 
               "http://127.0.0.1:8003/" + serviceName ];
    }
  }

  // Ratings is the microservice itself. It has one method so far, just 'get'.

  interface Ratings extends Service {
    // timeout, failureLimit, and retestDelay are the basic tunables for the RPC 
    // circuit-breaker/retry functionality.

    static float timeout = 1.0;
    static int failureLimit = 1;
    static float retestDelay = 30.0;

    // get: get the rating for a given thingID. Note that this call is 
    // _asynchronous_: Rating extends Future.

    Rating get(String thingID) {
      return ?self.rpc("get", [ thingID ]);
    }
  }

  // class RatingsClient extends roundrobin.RoundRobinClient, Ratings {}
  class RatingsClient extends Client, Ratings {}

  class RatingsServer extends Server<Ratings> {}
}
