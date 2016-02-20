## Datawire Connect Examples

Examples using only Quark features are available in the 
[Quark repository](https://github.com/datawire/quark/tree/master/examples).

Examples that demonstrate Datawire Connect and its associated cloud services 
are available in this repository.

### The helloRPC example

The [helloRPC](https://github.com/datawire/quark/tree/master/examples/helloRPC) example
is a very simple client-to-microservice interaction using an RPC pattern.

### The market example

The [market](https://github.com/datawire/datawire-connect/tree/master/examples/market)
example shows how to take an existing monolith application and connect it to a new
microservice. It also demonstrates how easy it is to get behaviors like timeouts, 
circuit breaking, and load balancing in your applications that consume microservices
built with Datawire Connect.

### The slack example

The [slack](https://github.com/datawire/quark/tree/master/examples/slack)
example illustrates how Quark can be used to build high level
interfaces for services that require rich interaction patterns. The
Slack service includes both a JSON RPC over HTTP
(https://api.slack.com) and a real-time API for processing events
(https://api.slack.com/rtm). Quark lets a service author easily create
and maintain rich clients for both these APIs. By describing the API
using Quark, the service author can quickly produce clients in
multiple languages that interface directly with this high level API
definition.

### The binary example

The [binary](https://github.com/datawire/quark/tree/master/examples/binary)
example illustrates how Quark can be used to provide an implementation
of an arbitrary binary websocket protocol that is accessible from
multiple languages.
