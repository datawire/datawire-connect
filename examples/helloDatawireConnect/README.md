# Hello Datawire Connect Example

This example demonstrates how Quark can implement cross-language RPC
using Datawire Connect.

## Setup

- `pip install datawire-cloudtools`
- create an org (`dwc create-org`)
- create a service named "hello" (`dwc create-service hello`)

You can use an organization you've already created. If you're creating
a new organization, it can be named whatever you like. The service,
however, _must_ be named `hello`, since that's what the example is 
expecting.

## Using Quark to Implement and Use Services

Datawire Connect uses the Quark language to express _service contracts_ in ways
that allow any of several host languages to easily implement and use services.
See QuarkAndDatawireConnect.md for (much) more information about using Quark in
your own projects.

## Hello Datawire Connect

The Hello Datawire Connect example implements and uses a very simple service:
the 'hello' service, on receiving a string from the client, echos back the string
it received, and what runtime the server is using.

The example supplies three different implementations:

- JavaScript under Node.js, in the `node` directory
- JavaScript in a browser, in the `browser` directory (client only)
- Python, in the `python` directory

## Running this example

The clients expect to find the service on http://127.0.0.1:8910/
and each server runs there. Thus you may run a single server at a
time, as well as any number of clients. You are encouraged to mix and
match languages! Any server should work with any client.

To get started, download the example by cloning its git repository as
follows:

        git clone https://github.com/datawire/quark.git

All of the directions below assume you are starting from
*repoBase*/examples/helloRPC where *repoBase* is the location where
you cloned the repository above.

### Reminder

You _must_ create a Datawire Connect organization and service, as described
above. The example code will not function unless it can find a service token
for a service named 'hello'.

### The Easy Way

Use the included Makefile to set up all three client/server pairs at once:

        make

Then follow the directions below to run one server, and try however many
clients you like.

### Python

To build just the Python implementation, you can use `make python`.

Run the Python server with

        python python/pyserver.py

Run the Python client with

        python python/pyclient.py

### Java

To build just the Python implementation, you can use `make java`.

Run the Java server with

        mvn exec:java -Dexec.mainClass=helloRPC.HelloRPCServer

Run the Java client with

        mvn exec:java -Dexec.mainClass=helloRPC.HelloRPCClient

### JavaScript under Node.js

To build just the Node.js implementation, you can use `make java`.

Run the Node.js server with

        node node/jsserver.js

Run the Node.js client with

        node node/jsclient.js

### JavaScript in a browser

To build just the JavaScript client for a browser, you can use `make browser`.

Run the client by opening `browser/hello.html` in your web browser.

There is no server for the browser. Instead, run the Node.js server:

        node node/jsserver.js
