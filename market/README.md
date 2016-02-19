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
