![Datawire](static-files/dw-logo.png)

# Datawire Connect

Datawire Connect is a simple way to build and run resilient microservices.

Datawire Connect allows you to fully express how microservices should connect to each other over the network. This includes:

* the interfaces between your services (e.g., expressing your REST or WebSockets API)
* how these interfaces should behave when they interact (e.g.,
  expressing your timeout / retry behavior over HTTP)
* how data is serialized on the wire (e.g., JSON)
* how clients should discover available services, and balance load across them

Datawire Connect works with your existing framework and languages. It does not require you to make changes to your existing interfaces, programming languages, or application framework. Datawire Connect has native support for Python, Java, and JavaScript, with Ruby and Go support coming soon.

## Features of Datawire Connect

* Native support for building resilient microservices in Python, JavaScript,
and Java (Ruby and Go support coming soon!)
* Automatic microservice registration with the Datawire Discovery cloud service
* Custom serialization support
* Support for HTTP/S, JSON, XML, Web Sockets...you name it
* A sophisticated language (Quark) that combines an IDL with a DSL, making it
very powerful for defining resilient service contracts

## Overview

Datawire Connect is built on [Quark](https://github.com/datawire/quark), a language designed for expressing the contract between services. Similar to a traditional IDL, Quark lets you define your service's APIs and how data is serialized. In this sense, Quark is similar to technologies such as [gRPC](http://www.grpc.io). Quark further extends the notion of a traditional IDL and lets you express protocol behaviors as part of your service contract. For example, you can also define how clients of that service should behave if the service is running slowly by adding circuit breakers, retry semantics, or backpressure to improve performance. There's no practical limit to the sophistication of the behaviors you could add to your microservices.

Datawire Connect also includes a cloud-based discovery service. This enables your clients and microservices to dynamically and securely discover each other, but without the overhead and cost of running your own discovery services. Datawire Discovery also provides an implementation of that service discovery system that can run locally. Since it is fully pluggable, it can support practically any other service discovery mechanisms based on technologies such as Zookeeper or Consul.

![Datawire Connect](static-files/dw-connect.png)

##Quick Start

We can use Datawire Connect to quickly add resilience to an existing HTTP-based microservice infrastructure. In this tutorial, we'll show how you add some [Hystrix](https://github.com/Netflix/Hystrix)-like resilience semantics (timeouts, load balancing, and circuit breakers) to HTTP-based RPC calls. We will also use the cloud-based Discovery Service.

### Installation

The following commands will install the Quark compiler, followed
by the Datawire Cloud command line tools:
```bash
$ pip install datawire-quark
$ pip install datawire-cloudtools
```
_Don't have ```pip```? Install it [here](https://pip.pypa.io/en/stable/installing/)._

Now you must create an organization in the Datawire Cloud to use the cloud-based
Discovery service:
```bash
$ dwc create-org <your organization> <your desired username> <your email>
```
For example, a user Alice working in Acme Corp might run the command as follows:
```bash
$ dwc create-org acme-corp alice alice@acme-corp.com
```
When the ```create-org``` command finishes, you will have a complete cloud-based
discovery service available for you to use.

### Running an Example

The first demo to try is the `market` demo, which shows a resilient RPC
interaction between an existing "monolithic" e-commerce web application
and a new microservice which adds a new feature to the system (product
ratings). It shows how easy it is to have the monolith changed to 
discover, locate and resiliently call the new ratings microservice.

To get the example code, simply clone this repository:
```bash
$ git clone https://github.com/datawire/datawire-connect.git
$ cd datawire-connect/examples/market
```
Then follow the instructions in the [README](https://github.com/datawire/datawire-connect/blob/master/examples/market/README.md)
to learn how to run the demo and to see cloud-based service discovery,
load balancing, timeouts, and circuit breaking in action.

## Learning More

You can try other examples within the 
[Quark repository](https://github.com/datawire/quark/tree/master/examples)
that showcase its power and flexibility for inter-service communication. 

The [```helloRPC```](https://github.com/datawire/quark/tree/master/examples/helloRPC)
demo shows basic 1-to-1 RPC, and how to implement clients and servers in any of Quark's
supported languages (Java, JavaScript, Python). There's also a demo that shows how to
use a custom serialization protocol, communicate with Web Sockets, and more. We've even
included an example of how to invoke an existing service with Datawire Connect using
the collaboration tool **Slack** as the wrappable service.

## Documentation 

You can read the Datawire Connect [documentation](http://datawire.github.io/quark/0.4/index.html) related to Quark. In particular, when you've reached the point of writing your own clients and services using Datawire Connect, you'll need our [language reference](http://datawire.github.io/quark/0.4/language-reference/index.html) that covers the Quark language constructs and syntax. You can also read documentation on our [command line cloud tools](http://datawire.github.io/datawire-connect/dev/0.4/cli/index.html).

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
