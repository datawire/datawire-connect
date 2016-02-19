The Datawire Market Example
===========================

This is the Datawire Market example, showing a very simple monolith and walking through how to switch it to use microservices.

The Market is written for Python 2.7. You _must_ use `virtualenv` to do everything the easy way. If you don't already have `virtualenv`, check out `https://virtualenv.readthedocs.org` to get it installed.

The Easy Way
------------

1. Create up and activate a virtualenv.
2. `make monolith`. This will set up your virtualenv with all the packages needed to run the monolith Market app, and start the Market running.
3. Point a web browser to `http://localhost:5000`.

You should see a Market offering four Things. You can add Things to your cart, and check out (which clears your cart, but doesn't do anything else).

Note that each Thing has a price, but no rating.

4. Kill everything with ^C.

Add Ratings
-----------

1. Create up and activate a virtualenv (it's OK to keep using the same one, if you already have one).
2. `make add-ratings`. This will make sure your virtualenv has everything you need to build the ratings service, build it, and start running a Market that will look for ratings.
3. Point a web browser to `http://localhost:5000`.

You should see pretty much the same thing as with the monolith now: prices, but no ratings. That's because no Ratings services are running yet.

4. In another window:
   1. Activate your virtualenv
   2. Get to the Market directory
   3. `make startRatings COUNT=3`

This will start three Ratings services running.

5. Refresh the web browser.

You should see all the ratings appear.

6. Simulate failure of the Ratings service:
   1. Use ^C to kill the Ratings services you started in step 4.
   2. `make startRatings COUNT=1`

This will start only one instance of the Ratings service.

7. Refresh the web browser.

All the ratings should still be present, but in the Market's output you should see that ratings are still trying to use all three instances:

```ASK for camera
- ratings using instance 2: http://127.0.0.1:8002/ratings
ASK for football
- ratings using instance 1: http://127.0.0.1:8001/ratings
```

and you should see some errors:

```BAD None: request timed out`

8. Before thirty seconds have passed, refresh the browser again.

This time you won't see any attempts to use instances 2 or 3, and all the requests should succeed. This happens because the circuit breakers for instances 2 and 3 opened when they failed, causing all requests to funnel to instance 1.

9. Wait thirty seconds. Refresh again.

This should behave exactly as in step 7: the breakers are reset to check if the dead services have come back to life.



