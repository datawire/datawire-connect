package ratings 0.0.1;
import builtin.concurrent;

class MyHub extends Hub {
  List<String> lookup(String serviceName) {
    return [ "http://127.0.0.1:8001/" + serviceName,
             "http://127.0.0.1:8002/" + serviceName, 
             "http://127.0.0.1:8003/" + serviceName ];
  }
}

// namespace alphaResilience {
//   class RoundRobinClient extends Client, Service {
//     List<String> urls;
//     int nextUp;

//     RoundRobinClient(List<String> urls) {
//       super(urls[0]);

//       self.urls = urls;
//       self.nextUp = 0;
//     }

//     String getURL() {
//       String url = self.urls[self.nextUp];

//       // print("using URL " + self.nextUp.toString() + ": " + url);

//       self.nextUp = self.nextUp + 1;

//       if (self.nextUp >= self.urls.size()) {
//         self.nextUp = 0;
//       }

//       return url;
//     }
//   }

//   class CharonService {
//     CharonService(URLSet urls, String myURL) {
//       self.urls = urls;
//       self.myURL = myURL;
//     }

//     String getURL() {
//       return self.myURL;
//     }

//     concurrent.Future rpc(String name, List<Object> args) {
//       behaviors.RPC rpc = new behaviors.RPC(self, name); // this could be allocated once per delegate instantiation

//       Future retval;
//       Future f2 = rpc.call(args);

//       f2.onFinished()

//       future = 
//       return rpc.call(args);
//     }    
//   }


//   class ResilientClientRPCCatcher extends concurrent.FutureListener {
//     URLSet urls;
//     concurrent.Future nextFuture;

//     ResilientClientListener(URLSet urls, concurrent.Future nextFuture) {
//       self.urls = urls;
//       self.nextFuture = nextFuture;
//     }

//     void onFuture(concurrent.Future result) {
//       String error = result.getError();

//       if (error != null) {
//         // Not so good.
//         self.urls.
//       }
//     }
//   }


//   class URLWithStatus {
//     String url;
//     integer up;

//     URLWithStatus(String url) {
//       self.url = url;
//       self.up = 1;
//     }

//     void markUp() {
//       self.up = 1;
//     }

//     void markDown() {
//       self.down = 1;
//     }
//   }

//   class URLSet {
//     List<URLWithStatus> urls;
//     int nextUp;
//     int numURLs;

//     URLSet(List<String> urls) {
//       for (int i = 0; i < urls.size(); i++) {
//         self.urls.add(new URLWithStatus(urls[i]));
//       }

//       self.nextUp = 0;
//       self.numURLs = self.urls.size();
//     }

//     void bumpNextUp() {
//       self.nextUp = (self.nextUp + 1) % self.numURLs;
//     }

//     String nextURL() {
//       int indexUsed = -1;
//       String url = null;
//       int tried = 0;

//       while (tried < self.urls.size()) {
//         if (self.urls[self.nextUp].up) {
//           indexUsed = self.nextUp;
//           url = self.urls[self.nextUp];
//           self.bumpNextUp();
//           break;
//         }

//         // This URL is marked down.
//         self.bumpNextUp();
//         tried = tried + 1;
//       }

//       if (url == null) {
//         print("No URLs are up!!");
//         return null;
//       }
//       else {
//         print("using URL " + indexUsed.toString() + ": " + url);
//         return url.url;
//       }
//     }

//     void markUp(String url) {
//       for (int i = 0; i < self.numURLs; i++) {
//         if (self.urls[i].url == url) {
//           self.urls[i].markUp();
//         }
//       }
//     }

//     void markDown(String url) {
//       for (int i = 0; i < self.numURLs; i++) {
//         if (self.urls[i].url == url) {
//           self.urls[i].markDown();
//         }
//       }
//     }
//   }

//   class ResilientClient extends Client, Service {
//     URLSet urls;

//     ResilientClient(List<String> urls) {
//       super(urls[0]);

//       self.urls = new URLSet(urls);
//     }

//     String getURL() {
//       return self.urls.nextAvailable();
//     }

//   }
// }

namespace ratings {
  // Rating is the data structure we'll be passing around between the microservice
  // and its client. It extends Future because the RPC can take awhile, and we don't
  // to block in the process.

  class Rating extends Future {
    String thingID;  // We include the thingID with its rating just to make it a
    int rating;    // little easier to keep track of what's what.
  }

  // Ratings is the microservice itself. It has one method so far, just 'get'.

  interface Ratings extends Service {
    // timeout, tripCount, and retryDelay are the basic tunables for the RPC 
    // circuit-breaker/retry functionality.

    static int timeout = 10000;
    static int tripCount = 3;
    static int retryDelay = 30000;

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
