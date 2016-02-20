![Datawire](static-files/dw-logo.png)

# Datawire Connect

Datawire Connect is a simple way to build and run resilient microservices.

Datawire Connect allows you to fully express how microservices should connect to each other over the network. This includes:

* the interfaces between your services (e.g., expressing your REST or WebSockets API)
* how these interfaces should behave when they interact (e.g.,
  expressing your timeout / retry behavior over HTTP)
* how data is serialized on the wire (e.g., JSON)

Datawire Connect works with your existing framework and languages. It does not require you to make changes to your existing interfaces, programming languages, or application framework. Datawire Connect has native support for Python, Java, and JavaScript, with Ruby support coming soon.

## Features of Datawire Connect

* Native support for building resilient microservices in Python, JavaScript,
and Java (Ruby and Go support coming soon!)
* Automatic microservice registration with the Datawire Discovery service
* Custom serialization support
* Support for HTTP/S, JSON, XML, Web Sockets...you name it
* A sophisticated language (Quark) that combines an IDL with a DSL, making it
very powerful for defining resilient service contracts

## Overview

Datawire Connect is built on [Quark](https://github.com/datawire/quark), a language designed for expressing the contract between services. Similar to a traditional IDL, Quark lets you define your service's APIs and how data is serialized. In this sense, Quark is similar to technologies such as[gRPC](http://www.grpc.io). Quark further extends the notion of a traditional IDL and lets you express protocol behaviors as part of your service contract. For example, you can also define how clients of that service should behave if the service is running slowly by adding circuit breakers, retry semantics, or backpressure to improve performance. There's no practical limit to the sophistication of the behaviors you could add to your microservices.

Datawire Connect also includes a native interface to service discovery. This interface enables microservices to dynamically discover and route data between each other. Datawire Discovery provides an implementation of the service discovery interface, but support for other service discovery mechanisms such as Zookeeper or Consul is supported in the design.

![Datawire Connect](static-files/dw-connect.png)

##Quick Start

We can use Datawire Connect to quickly add resilience to an existing HTTP-based microservice infrastructure. In this tutorial, we'll show how you add some [Hystrix](https://github.com/Netflix/Hystrix)-like resilience semantics (timeouts, load balancing, and circuit breakers) to HTTP-based RPC calls.

### Installation

The following command will install the Quark compiler and its runtime:
```
pip install datawire-quark
```
### Running an Example

The first demo to try is the `helloRPC` demo, which shows a simple RPC
interaction between a client and a microservice.

```
git clone https://github.com/datawire/quark.git
cd quark/examples/helloRPC
quark install hello.q --python
```

You should see the following:

```
Request says 'Hello from Python!'
Response says "Responding to 'Hello from Python!' from Datawire Cloud!"
```

#### Running the server locally  

Now it's time to run that same cloud server code in your own environment. Change the `pyclient.py` code to uncomment this line to make it refer to your local server:
```python
  client = hello.HelloClient(runtime, "http://127.0.0.1:8910/hello")

```
Run the local Python server with the command:
```
python pyserver.py
```
Then run the client with this command:
```
python pyclient.py
```
You should see the following in the client window:

```
Request says 'Hello from Python!'
Response says 'Responding to [Hello from Python!] from Python'
```
You'll see the full client / server interaction in your local environment.

#### Adding Resilience

If you look inside the service contract file `hello.q`, you'll see that this example already defines a default request timeout value of 3 seconds:

```java
    @doc("The hello service.")
    interface Hello extends Service {

	// How long (in seconds) the remote request is given to complete
        static float timeout = 3.0;
	// Number of failed requests before circuit breaker trips
        static int failureLimit = 1;
	// How long (in seconds) before circuit breaker resets
        static float retestDelay = 30.0;

        @doc("Respond to a hello request.")
        Response hello(Request request) {
	    // ? operator casts the return value to a Response object
            return ?self.rpc("hello", [request]);
        }

    }
```

To see this timeout being tripped, simply uncomment this line in `pyserver.py` to simulate a long processing time for the request:
```python
  import time; time.sleep(5)
```

Now re-run the Python server, re-run the client, and you'll see the client give up waiting for a response from the server after 3 seconds. Datawire Connect makes it trivial to add all kinds of important behaviors to your service contracts, from simple timeouts such as these to more complex things like circuit breakers.

## Learning more

Interested in adding a microservice to an existing monolith? Check out our online store example. The store is a monolith that adds a ratings microservice. If the microservice goes down the store still works without the ratings. As soon as the ratings service comes back the ratings appear again. You can also see which instance the rating is coming from and watch other instances repopulate the ratings when one of the instances goes down.

You can try other examples that show how to use a custom serialization protocol, communicate with Web Sockets, and more. We've even included a demo of how to invoke an existing service with Datawire Connect using the collaboration tool Slack as the wrappable service.

You can read the Datawire Connect[documentation](http://datawire.github.io/quark/0.4/index.html) related to Quark. In particular, when you've reached the point of writing your own clients and services using Datawire Connect, you'll need our [language reference](http://datawire.github.io/quark/0.4/language-reference/index.html) that covers the Quark language constructs and syntax.

## Supported Platforms

Datawire Connect has been certified on:

* Mac OS 10.10 (Yosemite)
* Mac OS 10.11 (El Capitan)
* Ubuntu 14.04 (Trusty)
* Fedora 22

## Roadmap

We have a [roadmap](https://github.com/datawire/datawire-connect/blob/master/ROADMAP.md).

## Getting Involved

Datawire Connect is open source and community-driven! Please feel free to raise GitHub issues as needed. If you'd like to make an enhancement or fix, please submit a Pull Request with your proposed changes. You can also join our [public Slack channel](https://datawire-quark.herokuapp.com/) for technical support and to interact with our development team.
