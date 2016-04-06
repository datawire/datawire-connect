# Python Hello Server example

import sys

import logging

logging.basicConfig(level=logging.DEBUG)

from datawire_connect.resolver import DiscoveryProvider as DWCProvider
from datawire_connect.state import DatawireState
from datawire_discovery.model import Endpoint as DWCEndpoint
from datawire_discovery.client import GatewayOptions as DWCOptions

import hello

######## SERVICE IMPLEMENTATION
class HelloImpl (object):
    """ The implementation of the Hello service itself. """

    def hello(self, request):
        """ Say hello! """

        # Snare a response object...
        res = hello.Response()

        # ...and fill it in.
        res.result = "Responding to [%s] from Python" % request.text

        # Uncomment the next line to simulate a long request processing
        # time (which may cause a timeout for the client, of course).
        # import time; time.sleep(5);

        # Mark our response as finished, so that when our caller gets
        # it, they know that everything that needs doing is done.
        res.finish(None)

        return res

######## MAINLINE
def main():
    # Grab our service token.
    dwState = DatawireState.defaultState()
    token = dwState.getCurrentServiceToken('hello')

    # Start our server running...
    url = "http://127.0.0.1:8910/"

    implementation = HelloImpl()
    server = hello.HelloServer(implementation)
    server.sendCORS(True)
    server.serveHTTP(url)

    # ...and then register it with Datawire Connect.
    endpoint = DWCEndpoint('http', '127.0.0.1', 8910, url)
    options = DWCOptions(token)

    provider = DWCProvider(options, "hello", endpoint)
    provider.register(15.0)

    logging.info("registered Python server on %s" % url)

if __name__ == '__main__':
    main()
