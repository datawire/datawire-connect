![Datawire](static-files/dw-logo.png)

# Datawire Connect

**Datawire Connect** helps you build and run resilient microservices.

It allows you to express the interfaces between your services, defines how they
should behave when they interact, and helps them reliably discover and reach
other services at runtime.

Datawire Connect is designed to work with your existing software and
languages. It does not require you to make changes to your existing
interfaces, programming languages, or application framework.

# Overview

A core part of Datawire Connect is **Quark**, a language that is used to define the
interfaces to your microservices and, more importantly, influence their runtime
behaviors. With Quark, you can specify much more than just the parameters of the
methods you create. You can also define how clients of that service should behave
if the service is running slowly, or add circuit breaking, or cache existing
response values to improve performance. There's no practical limit to the
sophistication of the behaviors you could add to your microservices.

Datawire Connect also includes client-side load balancing.

Discovery is achieved in Datawire Connect through **Datawire Hub**. This technology
offers your services a reliable and resilient way to register themselves so that
other services can find them.

![Datawire Connect](static-files/dw-connect.png)

## The Importance of Resilience

Resilience is crucial to the survival and growth of any microservice system.
As they get adopted within an organization and begin to handle more traffic,
more services get deployed, and at increasing speed.

However, without building in behavioral protections to your clients and services,
even a innocuous failure in your distributed system could prove devastating to
your entire application. It's therefore extremely important to design a
microservice-based system that is capable of handling failures, slowness, and offer
discovery, routing, serialization, asynchronicity, and more.

Datawire Connect can add resilience to any microservice system using the
powerful runtime behaviors that can be expressed in Quark, and through its
client-side load balancing capabilities.

## Getting Started in Minutes

Datawire Connect is super easy to install and use!

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
issues as needed, or talk to the experts on our public Slack channel.
If you'd like to make an enhancement or fix, please submit a Pull Request with
your proposed changes.
