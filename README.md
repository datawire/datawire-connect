![Datawire](static-files/dw-logo.png)

# Datawire Connect

**Datawire Connect** is a simple way to build and run resilient microservices.

Datawire Connect allows you to fully express how microservices should
connect to each other over the network. This includes:

* the interfaces between your services (e.g., expressing your REST or WebSockets API)
* how these interfaces should behave when they interact (e.g.,
  expressing your timeout / retry behavior over HTTP)
* how data is serialized on the wire (e.g., JSON)

Datawire Connect works with your existing framework and languages. It
does not require you to make changes to your existing interfaces,
programming languages, or application framework. Datawire Connect
has native support for Python, Java, and JavaScript, with Ruby support
coming soon.

# Overview

Datawire Connect is built on [Quark](https://github.com/datawire/quark),
a language designed for expressing the contract between services. Similar to a
traditional IDL, Quark lets you define your services APIs and how data is
serialized. In this sense, Quark is similar to technologies such as
[gRPC](http://www.grpc.io). Quark further extends the notion of a
traditional IDL and lets you express *protocol behaviors* as part of
your service contract. For example, you can also define how clients of
that service should behave if the service is running slowly by adding
circuit breakers, retry semantics, or backpressure to improve
performance. There's no practical limit to the sophistication of the
behaviors you could add to your microservices.

Datawire Connect also includes a native interface to service
discovery. This interface enables microservices to dynamically
discover and route data between each other. The **Datawire Hub**
provides an implementation of the service discovery interface, but
support for other service discovery mechanisms such as Zookeeper or
Consul is supported in the design.

![Datawire Connect](static-files/dw-connect.png)

# Quick Start

We can use Datawire Connect to quickly add resilience to an existing
HTTP-based microservice infrastructure. In this tutorial, we'll show
how you add some [Hystrix](https://github.com/Netflix/Hystrix)-like resilience
semantics (timeouts, load balancing, and circuit breakers) to HTTP-based
RPC calls.

#### Installation

The following command will install the Quark compiler and its runtime:
```
pip install datawire-quark
```
#### Running an Example

The first demo to try is the `helloRPC` demo, which shows a simple RPC
interaction between a client and a microservice.

```
git clone https://github.com/datawire/quark.git
cd quark/examples/helloRPC
quark install hello.q --python
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
Response says 'Responding to [Hello from Python!] from Python'
```

#### Learning more

The README.md in the `helloRPC` example directory will take the demo further by
showing you how to run the scenario in other languages such as Java and JavaScript.

You can also try the other included examples that show how to use a custom
serialization protocol, communicate with Web Sockets, and more. We've even
included a demo of how to invoke an existing service with Datawire Connect,
using the collaboration tool Slack as the wrappable service.

Datawire Connect has [extensive documentation](http://datawire.github.io/quark/0.4/index.html)
on all its features. When you've reached the point of writing your own clients
and services using Datawire Connect, you'll need our detailed
[language reference](http://datawire.github.io/quark/0.4/language-reference/index.html)
that covers the Quark language constructs and syntax in detail.

# Features of Datawire Connect

* Native support for building resilient microservices in Python, JavaScript,
and Java (Ruby and Go support coming soon!)
* Automatic microservice registration with the Datawire Discovery service
* Custom serialization support
* Support for HTTP/S, JSON, XML, Web Sockets...you name it
* A sophisticated language (Quark) that combines an IDL with a DSL, making it
very powerful for defining resilient service contracts

# Supported Platforms

Datawire Connect has been certified on:

* Mac OS 10.10 (Yosemite)
* Mac OS 10.11 (El Capitan)
* Ubuntu 14.04 (Trusty)
* Fedora 22

# Roadmap

We have a [roadmap](https://github.com/datawire/datawire-connect/blob/master/ROADMAP.md).

# Getting Involved

Datawire Connect is open source and community-driven! Please feel free to raise
GitHub issues as needed. If you'd like to make an enhancement or fix, please submit
a Pull Request with your proposed changes.
