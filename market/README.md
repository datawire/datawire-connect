This is the Datawire Market example, showing a very simple monolith and walking through how to switch it to use microservices.

The Market is written for Python 2.7. We strongly recommend using virtualenv!

1. To get started, you'll need Flask, Requests, and Nose:

        pip install flask requests nose

2. Run the completely monolithic Market, sans edits.

        cd datawire-examples/market
        python market.py

    This will start the Market running, displaying no ratings at all. It uses the monolithic database embodied by things.json.

3. With the Market running, fire up the tests.

        nosetests

    All tests should pass.
