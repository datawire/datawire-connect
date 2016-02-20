The Datawire Market Example
===========================

This is the Datawire Market example, showing a very simple monolith and walking through how to switch it to use microservices.

The Market is written for Python 2.7. You _must_ use `virtualenv` to do everything the easy way. If you don't already have `virtualenv`, check out `https://virtualenv.readthedocs.org` to get it installed.

The Monolith
------------

1. Create up and activate a virtualenv.
2. `make monolith`. This will set up your virtualenv with all the packages needed to run the monolith Market app, and start the Market running.
3. Point a web browser to `http://localhost:5000`.

You should see a Market offering four Things. You can add Things to your cart, and check out (which clears your cart, but doesn't do anything else).

Note that each Thing has a price, but no rating.

4. Kill everything with ^C.

Add Ratings
-----------

To use a microservice to add ratings to the Market, we first need to set up Datawire Connect:

1. Create up and activate a virtualenv (it's OK to keep using the same one, if you already have one).
2. `make datawire-connect`. This will make sure your virtualenv has everything you need for Datawire Connect.
3. Use Datawire Connect to create an organization and a service:
   1. `dwc create-org "My Test Org" your-name your-email-address
       1. You should supply your own name and email address. Feel free to supply a better organization name, too!
   1. `dwc create-service ratings`
       1. The name of the service must be 'ratings'.

Once that's done you can start up the Market:

1. `make add-ratings`. This will make sure your virtualenv has everything you need to build the ratings service, build it, and start running a Market that will look for ratings.
2. Point a web browser to `http://localhost:5000`.

You should see pretty much the same thing as with the monolith now: prices, but no ratings. That's because no Ratings services are running yet.

3. In another window (WINDOW 2):
   1. Activate your virtualenv
   2. Get to the Market directory
   3. `make startRatings COUNT=3`

This will start three Ratings services running.

4. Refresh the web browser.

You should see all the ratings appear.

5. Simulate complete failure of the Ratings service:
   1. Use ^C to kill the Ratings services you started in step 4.

6. Refresh the web browser.

All the ratings should still be present, but in the Market's output you should see that all the Ratings services are down:

```BAD None: all serivecs are down```

7. Start a single Ratings service in WINDOW 2:
   1. `make startRatings INSTANCE=1`

This will start one Ratings instance running.

8. Refresh the web browser.

All the ratings should still be present. In the Market's output you should see all the ratings requests using the single instance that's running:

```ASK for camera
DEBUG:DWC:DWC resolving ratings
DEBUG:DWC:DWC resolved ratings => [http://127.0.0.1:8001]
INFO:quark.client:- ratings using instance 1: http://127.0.0.1:8001
```

9. In another window (WINDOW 3), start another instance of the Ratings service:
   1. Activate your virtualenv
   2. Get to the Market directory
   3. `make startRatings INSTANCE=2`

This will start a second Ratings instance running.

10. Refresh the web browser.

All the ratings should still be present. In the Market's output you should see the ratings requests interleaving between the two instances that are running:

```ASK for camera
DEBUG:DWC:DWC resolving ratings
DEBUG:DWC:DWC resolved ratings => [http://127.0.0.1:8001, http://127.0.0.1:8002]
INFO:quark.client:- ratings using instance 1: http://127.0.0.1:8001
ASK for basketball
DEBUG:DWC:DWC resolving ratings
DEBUG:DWC:DWC resolved ratings => [http://127.0.0.1:8001, http://127.0.0.1:8002]
INFO:quark.client:- ratings using instance 2: http://127.0.0.1:8002
```

11. Pause, but do not kill, Ratings service #2:
  1. In WINDOW 2, hit ^Z.

At this point the second instance is running but unresponsive.

12. Refresh the web browser.

All the ratings should still be present, but in the Market's output you should see errors about the unresponsive instance.

```
ASK for football
DEBUG:DWC:DWC resolving ratings
DEBUG:DWC:DWC resolved ratings => [http://127.0.0.1:8001, http://127.0.0.1:8002]
INFO:quark.client:- ratings using instance 2: http://127.0.0.1:8002
WARNING:quark.client:- OPEN breaker on [ratings at http://127.0.0.1:8002]
...
WAITED 1090ms
BAD None: request timed out
```

13. Before thirty seconds have passed, refresh the web browser again.

This time all requests should go to instance 1, and they should all succeed.

14. Wait thirty seconds, then restart instance 2.
  1. In WINDOW 1, run `fg` to restart the paused process.

This will simulate the unresponsive instance recovering. You may see some old requests suddenly appear in WINDOW 2, which is OK. 

Once the instance is resumed, it should send a heartbeat within 15 seconds. At that point you should see the Market indicating that it sees that the instance is alive again:

```INFO:quark.client:- CLOSE breaker on [ratings at http://127.0.0.1:8002]```

15. Refresh the web browser.

Once again, requests should be interleaved between the two instances, and all should succeed.
