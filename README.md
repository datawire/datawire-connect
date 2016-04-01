![Datawire](static-files/dw-logo.png)

## Datawire Connect
[![Build Status](https://travis-ci.org/datawire/quark.svg?branch=master)](https://travis-ci.org/datawire/quark)
[![Slack](https://datawire-quark.herokuapp.com/badge.svg?dummy)](https://datawire-quark.herokuapp.com)

Datawire Connect is a simple, powerful way to resiliently connect
microservices. Datawire Connect natively integrates into your existing
Java, Python, or NodeJS application (Ruby coming soon), and provides:

* service registration and discovery
* dynamic load balancing and routing
* automatic timeouts
* integrated circuit breakers

Moreover, Datawire Connect provides these semantics without requiring
you to modify any of your existing HTTP/REST APIs.

## Example

Suppose you have an existing service *A*, with a REST
interface. Further suppose you have an existing service, *B*, that
calls *A*. To maximize the resilience of the overall system, you want
to minimize the impact of any downtime of *A* on *B*.

Using Datawire Connect, you can code the existing API for *A*
in Quark, the Interface Definition Language (IDL) used by Datawire
Connect. Datawire Connect will then compile your Quark file into
native client libraries that can be used by *B*.

*B* can now use API calls in its native language (e.g., Python). Each
of these API calls will automatically integrate resilience patterns,
including circuit breakers, timeouts, and load balancing.

## Quick Start

Datawire Connect includes sample code that illustrates the above
example. By default, Datawire Connect integrates with the Datawire
Cloud Discovery service, although this is easily changed.

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
the collaboration tool Slack as the wrappable service.

## Documentation 

You can read the Datawire Connect [documentation](http://datawire.github.io/quark/0.4/index.html) related to Quark. In particular, when you've reached the point of writing your own clients and services using Datawire Connect, you'll need our [language reference](http://datawire.github.io/quark/0.4/language-reference/index.html) that covers the Quark language constructs and syntax. You can also read documentation on our [command line cloud tools](http://datawire.github.io/datawire-connect/0.4/cli/index.html).

## Supported Platforms

Datawire Connect has been certified on:

* Mac OS 10.10 (Yosemite)
* Mac OS 10.11 (El Capitan)
* Ubuntu 14.04 (Trusty)
* Fedora 22

## Architecture

Datawire Connect is built on
[Quark](https://github.com/datawire/quark), a language designed for
expressing the contract between services. Similar to a traditional
IDL, Quark lets you define your service's APIs and how data is
serialized. In this sense, Quark is similar to technologies such as
[gRPC](http://www.grpc.io). Quark further extends the notion of a
traditional IDL and lets you express protocol behaviors as part of
your service contract. For example, you can also define how clients of
that service should behave if the service is running slowly by adding
circuit breakers, retry semantics, or backpressure to improve
performance. There's no practical limit to the sophistication of the
behaviors you could add to your microservices.

Datawire Connect also integrates with Datawire Cloud Discovery, a
cloud-based discovery service. This enables your clients and
microservices to dynamically and securely discover each other, but
without the overhead and cost of running your own discovery
services. (If you want to use your local Discovery service, we also
have open sourced the [Discovery
service](https://github.com/datawire/discovery)]. It's fully
plugabble, so it supports strongly consistent data stores such as
Zookeeper or Consul.)

![Datawire Connect](static-files/dw-connect.png)

## Roadmap

We have a [roadmap](https://github.com/datawire/datawire-connect/blob/master/ROADMAP.md).

## Alternatives

If you're trying to add resilience to your microservices architecture
and don't want to use Datawire Connect, there are some other popular
choices:

* Use HTTP with other resilience libraries, e.g.,
  [Hystrix](https://github.com/Netflix/Hystrix/) and
  [Eureka](https://github.com/Netflix/eureka). Datawire Connect takes
  heavy inspiration from these libraries, which are Java-centric.
  
* [gRPC](http://www.grpc.io/). This is not backwards-compatible with
  your existing REST interfaces, but multiple languages are
  supported.

* Use an async messaging bus, such as [NATS](http://nats.io) or
  [RabbitMQ](http://www.rabbitmq.com/). This does require you to
  switch your interaction model from RPC to async, which may impact
  your overall system architecture.


## Getting Involved

Datawire Connect is open source and community-driven! Please feel free
to raise GitHub issues as needed. If you'd like to make an enhancement
or fix, please submit a Pull Request with your proposed changes. You
can also join our [public Slack
channel](https://datawire-quark.herokuapp.com/) for technical support
and to interact with our development team.

