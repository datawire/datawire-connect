# The Datawire Market Example

This example starts with a simple monolithic application, and walks through how to change it to resiliently call a new microservice.

The monolith being demonstrated is a mock e-commerce application. It allows the user to put some items in a cart and then checkout to purchase them. However, the items being displayed have no user ratings associated with them, and the engineers behind the monolith have decided to create a **product ratings microservice** to add this feature (as opposed to adding all the ratings logic directly into the existing monolithic web application).

The engineers therefore need to connect their monolith to this new microservice, but do so in a way that is resilient and performant.

### Prerequisites

You should have followed the installation instructions in the Datawire Connect [README](https://github.com/datawire/datawire-connect/blob/master/README.md).

The Market is written for Python 2.7. You should always use `virtualenv` with Python applications. If you don't already have `virtualenv`, you should [get it installed](https://virtualenv.readthedocs.org) and use it throughout this demo.

### Run The Monolith

In a terminal window (which we'll call WINDOW 1):

1. Create and activate a virtualenv.
2. `make monolith`. This will set up your virtualenv with all the packages needed to run the monolith Market app, and start the Market running.
3. Point a web browser to http://localhost:5000.
4. You should now see the Datawire Market web app, and that it offers four items for sale. You can add items to your cart, and check out (which clears your cart, but doesn't do anything else). Note that each item has a price, but currently has no rating.
5. Kill the market server with ^C.

### Register the Ratings Microservice

The code for the product ratings microservice has already been written, so it just needs to be launched. However you will need to make sure your Datawire cloud system is active since it is used for service registration and discovery.

In terminal WINDOW 1:

1. Create and activate a virtualenv (it's OK to keep using the same one, if you already have one).
2. If you haven't already installed the Datawire Connect CLI, `make install-dwc`. This will make sure your virtualenv has everything you need for Datawire Connect.
3. If you haven't already created a Datawire Connect organization, do so now:
   * `dwc create-org "My Test Org" your-name your-email-address`
       * _You should supply your own name, email address and organization._
4. Now create a new service registration entry for the ratings microservice:
   * `dwc create-service ratings`
       * Note: the name of the service **must** be `ratings`, since that's the service name that the monolith will try to discover and call.

### Connect the Market App to the Ratings Microservice

Now we will start up a new version of the Market app that is coded to discover and call the ratings service.

Still in terminal WINDOW 1:

1. If you haven't already installed Quark, `make install-quark`. This will make sure you have the Quark language compiler installed.
1. `make add-ratings`. This will make sure your virtualenv has everything you need to build the ratings service, build it, and start running the new Market app that will try to get ratings for each item whenever the page is loaded.
2. Point a web browser to http://localhost:5000.

You should see pretty much the same thing as with the original Market monolith now: you can see prices, but no ratings. That's because no Ratings services are running yet.

### Launch the Ratings Microservice

In another window (WINDOW 2):

1. Activate your virtualenv
2. Change to the Market example directory
3. Run the command: `make startRatings COUNT=3`
 * This will launch three instances of the ratings service in that window.
4. Refresh the web browser window.

You should now see ratings appear next to each item for sale. If you look in the console output in WINDOW 1, you can see the market app make 4 individual calls to retrieve the ratings for each item.

## Seeing Resilience in Action

Now that everything is up and running, let's see what happens when we introduce failures into the system.

#### Total Service Failure

We will simulate complete failure of the ratings service by simply stopping it.

1. Use ^C to kill the Ratings services you started in WINDOW 2.
2. Refresh the web browser.

All the ratings should still be present as the web application has been coded to cache values that were retrieved recently. However in the Market's console output (WINDOW 1) you should see that all the Ratings services are down:

```BAD None: all services are down```

#### Load Balancing

This example uses a round-robin load balancing strategy for ease of demonstration.

1. Start a single Ratings service in WINDOW 2:
   * Run the command: `make startRatings INSTANCE=1`
   * This will launch just one instance of the ratings service.
2. Refresh the web browser.

All the ratings should still be present with each item. In the Market's output (WINDOW 1) you should see all the ratings requests using the single instance that's running:
```
INFO:quark.client:- ratings using instance 1: http://127.0.0.1:8001
```

In yet another window (WINDOW 3), start another instance of the Ratings service:

3. Activate your virtualenv
4. Change to the Market directory
5. Run the command: `make startRatings INSTANCE=2`

This will start a second Ratings instance running. 

Now refresh the web browser, and all the ratings should still be present. In the Market's output (WINDOW 1), you should see the ratings requests interleaving between the two instances that are running:

```
INFO:quark.client:- ratings using instance 1: http://127.0.0.1:8001
...
INFO:quark.client:- ratings using instance 2: http://127.0.0.1:8002
```

#### Circuit Breaking

Circuit Breaking is a technique in distributed systems where the detection of a faulty service instance causes all requests to that endpoint to fail for a period of time. When this occurs, the circuit is said to be open, and requests to that service instance will not be attempted. When the configured amount of time passes (30 seconds in this example), the circuit closes and requests to that service are attempted again.

* Pause, but do not kill, instance #1 of the Ratings service:
  * In WINDOW 2, hit ^Z. 

At this point, the instance is still running, but it will not respond to requests.

* Refresh the web browser.

All the ratings should still be present -- not only is service instance 2 still running (in WINDOW 3), but the ratings are cached too. In the Market's output (WINDOW 1), though, you should see errors about the unresponsive instance:

```
INFO:quark.client:- ratings using instance 1: http://127.0.0.1:8001
WARNING:quark.client:- OPEN breaker on [ratings at http://127.0.0.1:8001]
```

* Before thirty seconds have passed, refresh the web browser again.

This time all requests should go to instance 2, and they should all succeed. By using Datawire Connect, the market app was able to avoid lots of wasted effort trying to reach service instance 1.

After thirty seconds, you should see (in WINDOW 1) that the Market is willing to retry instance 1:

```
WARNING:quark.client:- RETEST breaker on [ratings at http://127.0.0.1:8001]
```

* At that point, restart instance 1.
  * In WINDOW 2, run `fg` to restart the paused process.

This will simulate the unresponsive instance recovering. You should see the Market indicating (in WINDOW 1) that it sees that the instance is alive again:

```
INFO:quark.client:- ratings using instance 1: http://127.0.0.1:8001
INFO:quark.client:- CLOSE breaker on [ratings at http://127.0.0.1:8001]
```

* Refresh the web browser.

Once again, requests should be interleaved between the two instances, and all should succeed.

## Writing your own microservice

You can use this demo as a way to write your own microservice(s). In this example:

1. We wrote a standard web application using Python and Flask ([add-ratings/market.py](https://github.com/datawire/datawire-connect/blob/master/examples/market/add-ratings/market.py)) to simulate an existing monolith. If you have an existing monolith, you don't need to write another one :-).

2. We then defined the service contract in the Quark language for the ratings microservice. The ratings microservice's contract is within [ratings.q](https://github.com/datawire/datawire-connect/blob/master/examples/market/ratings/ratings.q), and it describes both the API signatures for the service as well as how clients should behave when calling them.

   The API signatures are as follows:

   ```
   // Data structure that gets passed around
   class Rating extends Future {
   	 String thingID;
	 int rating;
   }

    // API signature
   Rating get(String thingID) {
       return ?self.rpc("get", [ thingID ]);
   }
    ```

    The ratings.q contract file also contains configuration for request timeouts, failure limits and circuit breaking periods:

   ```
       static float timeout = 1.0;      // per-request timeout
       static int failureLimit = 1;     // number of successive request failures before the circuit breaker opens
       static float retestDelay = 30.0; // how long to wait until closing the circuit breaker and retrying
   ```

3. We then update the monolith to call the ratings microservice. You can see the changes made by running `diff` between [add-ratings/market.py](https://github.com/datawire/datawire-connect/blob/master/examples/market/add-ratings/market.py) and [monolith/market.py](https://github.com/datawire/datawire-connect/blob/master/examples/market/monolith/market.py).

    In a nutshell, calling a service was as simple as this:

    ```Python
    # add-ratings/market.py 
    ratings = RatingsClient("ratings")
    ...
    ratings.get(thingID)
    ```

    However there was some extra code used in the example to allow the application to call the ratings API concurrently rather than serially, and to cache responses in the case where no services are available at all. But the basic act of calling a service was as simple as what is shown above.
