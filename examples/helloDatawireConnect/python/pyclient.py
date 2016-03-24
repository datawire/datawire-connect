# Python Hello Client example

import sys

import logging

logging.basicConfig(level=logging.DEBUG)

from datawire_connect.resolver import DiscoveryConsumer as DWCResolver
from datawire_discovery.client import GatewayOptions as DWCOptions
from datawire.utils.state import DataWireState, DataWireError

import hello

def main():
    # Set up the client...
    client = hello.HelloClient("hello")

    # ...and feed it a resolver for Datawire Connect.

    options = DWCOptions(DataWireState().currentServiceToken('ratings'))

    client.setResolver(DWCResolver(options))

    # OK, make the call!   
    request = hello.Request()

    if len(sys.argv) > 1:
        request.text = str(sys.argv[1])
    else:
        request.text = "Hello from Python!"

    print "Request says %r" % request.text

    response = client.hello(request)
    response.await(1.0)

    if not response.isFinished():
        print "No response!"
    elif response.getError() is not None:
        print "Response failed with %r" % response.getError()
    else:
        print "Response says %r" % response.result

if __name__ == '__main__':
    main()
