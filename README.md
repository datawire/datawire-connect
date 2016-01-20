![Datawire](static-files/dw-logo.png)

# Datawire Connect

**Datawire Connect** is a simple way to build and run resilient microservices.

Datawire Connect allows you to fully express the contract between
services. This includes:

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

Datawire Connect is built on **Quark**, a language designed for
expressing the contract between services. Similar to a traditional
IDL, Quark lets you define your services APIs and how data is
serialized. In this sense, Quark is similar to technologies such as
GRPC. Quark also extends the notion of a traditional IDL and lets you
express *protocol behaviors* as part of your service contract. For
example, you can also define how clients of that service should behave
if the service is running slowly, add circuit breaking, or cache
existing response values to improve performance. There's no practical
limit to the sophistication of the behaviors you could add to your
microservices.

Datawire Connect also includes a native interface to service
discovery. This interface enables microservices to dynamically
discover and route data between each other. The **Datawire Hub**
provides an implementation of the service discovery interface, but
support for other service discovery mechanisms such as Zookeeper or
consul.io is supported in the design.

![Datawire Connect](static-files/dw-connect.png)

# Quick start

You can use Datawire Connect to quickly add resilience (timeouts,
circuit breakers, and load balancing) to your existing HTTP-based
microservice infrastructure.

#### Installation
```
pip install datawire-quark
```
#### Running an Example

The first demo to try is the `helloRPC` demo. We have a microservice running in
the cloud that you can call using the `helloRPC` client example:

```
cd datawire-quark/examples/helloRPC
quark --python package hello.q
pip install hello/py/dist/hello-0.1.0-py2-none-any.whl
python pyclient.py
```
You should see the following:

```
Response says "Responding to 'Hello from Python!' from Datawire Cloud!"
```

## Learning more

The [Getting Started with RPC tutorial](http://datawire.github.io/quark/0.3/tutorials/rpc-basic/index.html)
will take the `helloRPC` example further by showing you how to run your own local
server, and how to do so in other languages such as Java and JavaScript.

You can also try the other included examples that show how to use a custom
serialization protocol, communicate with Web Sockets, and more. We've even
included a demo of how to invoke an existing service with Datawire Connect,
using the collaboration tool Slack as the wrappable service.

When you've reached the point of writing your own clients or services using
Datawire Connect, you'll need our detailed [language reference](http://datawire.github.io/quark/0.3/language-reference/index.html)
that covers the Quark language constructs and syntax in detail.

## Features of Datawire Connect

* Native support for building resilient microservices in Python, JavaScript,
and Java (Ruby and Go support coming soon!)
* Automatic microservice registration with the Datawire Hub discovery service
* Custom serialization support
* Support for HTTP/S, JSON, XML, Web Sockets...you name it
* A sophisticated language (Quark) that combines an IDL with a DSL, making it
very powerful for defining resilient service behaviors

## Roadmap

Lots of exciting features are currently being developed for Datawire Connect,
including:

* Support for Ruby and Go
* Cloud-based version of Datawire Hub
* Per-service timeouts (aka, circuit breaking)
* Intelligent load balancing

For more information, read our more detailed [roadmap](https://github.com/datawire/quark/blob/master/ROADMAP.md).

# Getting Involved

Datawire Connect is open source and community-driven! Please feel free to raise 
GitHub issues as needed. If you'd like to make an enhancement or fix, please submit
a Pull Request with your proposed changes.
