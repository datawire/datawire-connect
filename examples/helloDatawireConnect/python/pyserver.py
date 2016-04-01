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

        # Uncomment the next line to simulate a long request processing
        # time and force a request timeout to occur for the client.
        # import time; time.sleep(5)

        # Once that's done, snare a response object...
        res = hello.Response()

        # ...fill it in...
        res.result = "Responding to [%s] from Python" % request.text

        # ...and finish it.
        res.finish(None)

        return res

######## MAINLINE
def main():
    dwState = DatawireState.defaultState()
    token = dwState.getCurrentServiceToken('hello')

    url = "http://127.0.0.1:8910/"

    implementation = HelloImpl()
    server = hello.HelloServer(implementation)
    server.serveHTTP(url)

    endpoint = DWCEndpoint('http', '127.0.0.1', 8910, url)
    options = DWCOptions(token)

    provider = DWCProvider(options, "hello", endpoint)
    provider.register(15.0)

if __name__ == '__main__':
    main()
