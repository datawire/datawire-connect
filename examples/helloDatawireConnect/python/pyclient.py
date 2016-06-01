# Python Hello Client example

import sys

import logging
import time

logging.basicConfig(level=logging.INFO)

from datawire_connect.resolver import DiscoveryConsumer as DWCResolver
from datawire_connect.state import DatawireState
from datawire_discovery.client import GatewayOptions as DWCOptions

import hello

def main(text):
    # Grab our service token.
    dwState = DatawireState.defaultState()
    token = dwState.getCurrentServiceToken('hello')

    # Set up the client...
    client = hello.HelloClient("hello")

    # ...and tell it that we want to use Datawire Connect to find 
    # providers of this service.
    options = DWCOptions(token)
    client.setResolver(DWCResolver(options))

    # Give the resolver a chance to get connected.
    time.sleep(5);

    # OK, make the call!   
    request = hello.Request()
    request.text = text

    print "Request says %r" % request.text

    response = client.hello(request)
    response.await(1.0)

    if not response.isFinished():
        print "No response!"
    elif response.getError() is not None:
        print "Response failed with %r" % response.getError()
    else:
        print "Response says %r" % response.result

    print("")
    print("")
    print("You need to interrupt me to exit at the moment, sadly.")
    print("The resolver thread isn't marked as a daemon, so it's")
    print("still lingering around.")

if __name__ == '__main__':
    text = "Hello from Python!"

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])

    main(text)
