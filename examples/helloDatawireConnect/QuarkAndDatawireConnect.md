# Using Quark and Datawire Connect

Datawire Connect uses the Quark language to express _service contracts_ in ways
that allow any of several host languages to easily implement and use services.
The service contract defines not just the data sent between the client and the
server, but also behaviors required of each side of the transaction.

The service-contract concept allows Datawire Connect to tackle some very hard
problems with relative ease, but as with any toolset, it's important to start
with a good basic grounding of how all the pieces fit together.

## The `Service` Interface

The core of the service contract is the `Service` interface, which is
meant to be extended by classes that define the various things that
the service is prepared to do for the client. Each of these 'verbs'
should be a method defined by the interface extending `Service`.

Using Hello Datawire Connect as an example, this is the bare-bones
version of the service interface:

```
namespace hello {
	// Request is data from the client to the server
    class Request {
        String text;
    }

	// Response is data from the server to the client
    class Response extends Future {
        String result;
    }

    // The Hello interface defines the things the client
    // can request.
    interface Hello extends Service {
        Response hello(Request request) {
		    // ? operator casts the return value to a Response object
            return ?self.rpc("hello", [request]);
        }
    }
}
```

which defines a single method, `hello`, which does a simple RPC call.

The `hello` method accepts a `hello.Request` object, and returns a
`hello.Response` object.

## `Future` Objects

Note that `hello.Response` extends `Future`. This is Quark's mechanism
for handling the asynchronicity typical of microservice environments.
Objects extending `Future` (here called `Future`s) represent data that
will be available at some point in the future, although it might not be
available just yet.

When a `Future` is instantiated, it is marked _unfinished_. Whenever its
creator decides that it's ready, it can _finish_ the `Future` by calling
its `finish` method. In the success case, `finish` is called with no
argument; for errors, `finish` is called with a `String` describing the
error.

You may check if a `Future` has been finished by calling its `isFinished`
method, but the real power of a `Future` is that you can attach delegate
objects to it by passing them to the `Future`'s `onFinished` method. When
the `Future` is resolved or rejected, all of its delegate objects have 
their `onFuture` method called with the `Future` as their sole parameter.

## Client and Server Adapters

The service contract isn't much good without providing clients and servers
that obey the contract. To enable code in your host language to interact
with the Quark code defining the contract, you define client and server
adapters, which are classes that provide the glue code to let everything
work smoothly.

### Client Adapters

Client adapters extend Quark's `Client` interface _and_ your service
interface, for example:

```
class HelloClient extends Client, Hello {}
```

Typically, the functionality provided by Quark's default `Client` class 
is sufficient, and you won't need to write custom code -- hence the `{}`
class body for `HelloClient`.

### Server Adapters

Server adapters extend the `Server<Service>` interface, which uses Quark's
templating capability to define an adapter for a specific service
interface. For example, for Hello Datawire Connect, the single line

```
class HelloServer extends Server<Hello> {}
```

defines a server adapter specifically for the `Hello` service interface. 

Typically, the functionality provided by Quark's default `Server` class 
is sufficient, and you won't need to write custom code -- hence the `{}`
class body for `HelloServer`.

## Adapters and Resolvers

When you instantiate a client or server adapter class, you must give it both
a service name and a _resolver_ object. It's the job of the resolver to map
between service names and URLs where those services can be found:

- a client adapter uses its resolver to take a service name and look up the
URL that the client will use to make requests of the service, and
- a server adapter uses its resolver to tell others which service is available
at its URL.

The default resolver assumes that the service name _is_ a URL. To use Datawire
Connect, however, you need to supply a resolver that understands how to look
up service names using the Datawire Connect Discovery service. These resolvers
are defined in `datawire-connect-1.0.0.q`:

- `datawire_connect.resolver.DiscoveryConsumer` is a resolver for a client. It
uses Datawire Connect's Discovery service to look up the URL for a given service.
- `datawire_connect.resolver.DiscoveryProvider` is a resolver for a server. It
uses Datawire Connect's Discovery service to register a URL for a given service.

Both of these resolvers need to be instantiated with the service token as well
as the service name. At the moment, the service token is contained in a 
`datawire_discovery.client.GatewayOptions` object, which is defined in
`discovery-1.0.0.q`. This will be changing in the future.

# Writing a client

Given the service contract, it's fairly easy to write a client of the 
service. Here's the basic pattern:

- Pull in the service contract and your service token
- Initialize Datawire Connect
- Create a client instance using your client adapter
- Make calls using the client instance.

## The Service Contract in the Client

When you compile the service contract, it is installed as a package that can
be imported into your client code in whatever way is appropriate for your host
language: `import` for Python and Java, `require` for JavaScript, etc.

Pulling the `Hello` service contract in makes the `hello` namespace available 
to the host language. In particular, the `HelloClient` class becomes available,
so that the host language can make requests of the service.

## Initializing Datawire Connect

Initializing Datawire Connect in the client is basically a matter of creating
the resolver object. At the moment, this requires also creating the options
object as mentioned above in 'Adapters and Resolvers'.

Note that creating the resolver requires the service token. The way the service
token is obtained depends on the host language, but in general it should be
loaded from the state maintained by the `dwc` command.

For Hello Datawire Connect, all of the clients create a `DiscoveryConsumer`
resolver, since the client code is only making requests. 

## Creating the Client Instance

For Hello Datawire Connect, this is nearly as simple as instantiating a
`HelloClient` object. However, after instantiating the object, it's necessary
to use `client.setResolver` to tell the client which resolver object to use.

## Making Calls

The 'Hello' service contract only has one verb, and thus its client adapter 
only has the single method `hello`. Making a call to the service - including
circuit breaking and load balancing between multiple service providers - is
literally as simple as calling the `hello` method.

The return value from the `hello` method is a `HelloResponse` object, which
is a `Future`. Therefore, all the clients use the response's `onFinished`
method to associate a delegate, to avoid inefficient busy waiting.

# Writing a server

Given the service contract, the server follows a pattern roughly similar to
the client:

- Pull in the service contract and your service token
- Initialize Datawire Connect
- Set up the host-language service implementation
- Start the server running
- Create a server instance using your server adapter

## The Service Contract in the Server

Pulling in the `Hello` service contract works the same in the server as in
the client. However, the critical thing for the server is the `HelloServer`
class, which allows the server to respond to requests.

## Initializing Datawire Connect

Initializing Datawire Connect in the server is also basically the same as 
in the client. The main difference for Hello Datawire Connect is that the
servers create a `DiscoveryProvider` resolver, since they are providing the
'Hello' service rather than making requests of it.

## The Host-Language Service Implementation

This is where the server and client diverge significantly. The server
adapter requires you to pass in an implementation object that will do the
heavy lifting of providing the service. This object must implement the 
entirety of the service contract, specifically including all the verb 
methods.

For Hello Datawire Connect, this means that we must provide an object that
implements the `Hello` interface.

### Request and Response Objects

The verb methods will typically accept a request object, and return a
response object. Request objects can be of nearly any type, but response
objects _must extend `Future`_ in order to manage asynchronicity.

It is the responsible of the service implementation to `finish` each 
response object. In many situations it will be possible to `finish` the
response before returning from the verb method (this is what Hello
Datawire Connect does, for example). In more complex situations, the 
server implementation might start a new thread before returning the
response object, and then that thread will eventually `finish` the 
response object.

### Host Languages and Typing

Note that Quark and the host language typically do not exchange typing
information! Therefore, the details of the implementation object vary with
the host language.

#### Python

In Python, Quark relies on duck typing for the implementation object. It's
simplest to use a class derived from `object`, with an instance method for
each verb:

```
class HelloImpl(object):
    def hello(self, request):
        ...

implementation = HelloImpl()
server = hello.HelloServer(implementation)
```

#### JavaScript

In JavaScript, Quark expects the implementation object to be an actual
object, to avoid issues with the meaning of `this`:

```
var HelloImpl = (function () {
	function HelloImpl() {}

	HelloImpl.prototype.hello = function (request) {
		...
	};

	return HelloImpl;
})();

var implementation = new HelloImpl();
var server = new hello.HelloServer(implementation);
```

#### Java

Unsurprisingly, Java has the strictest typing requirements. The various
classes and interfaces must be explicitly imported, and the implementation
object must be correctly typed:

```
import hello.Hello;
import hello.Request;
import hello.Response;

public class HelloImpl extends quark.BaseService implements Hello {
	@Override
	public Response hello(Request request) {
		...
	}
}
```

Then, in the server's source file:

```
import hello.HelloServer;

...

HelloImpl impl = new HelloImpl();
HelloServer server = new HelloServer(impl);

...
```

## Starting the Server

Once the service implementation object is created, _that_ is the point at 
which to start listening for network traffic. The details of how you best
do this will, of course, vary dramatically with your host language, etc.

However, a simple option is the `serveHTTP` method on the server adapter,
which will start listening for traffic in a way that's suitable for debugging
but probably not for high-volume services. Hello Datawire Connect uses this
method.

## Creating the Server Instance

_After_ the server is listening for network traffic, you need to register
your service with Datawire Connect. Registering requires a few steps at
present:

- create a `datawire_discovery.model.Endpoint` object detailing where your
service can be found
- create a `datawire_discovery.client.GatewayOptions` object containing your
service token
- create a `datawire_connect.resolver.DiscoveryProvider` object and call its
`register` method

