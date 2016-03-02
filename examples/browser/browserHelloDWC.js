// var builtin = require('builtin').builtin;
// var runtime = builtin.concurrent.Context.runtime()

// Snare the "Hello Datawire Connect" service contract...
var hello = require("hello").hello;

// ...initialize our token...
var token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJkd1R5cGUiOiJEYXRhV2lyZUNyZWRlbnRpYWwiLCJlbWFpbCI6bnVsbCwianRpIjoiOTcyNmJlOWQtYTVjMS00NmYxLWJlYTgtN2I0MGY2ODVjYzE2IiwiYXVkIjoiNFg1WjJGSjI4RiIsInNjb3BlcyI6eyJkdzpzZXJ2aWNlMCI6dHJ1ZX0sImlzcyI6ImNsb3VkLWh1Yi5kYXRhd2lyZS5pbyIsImlhdCI6MTQ1NTg1NzE2NSwib3duZXJFbWFpbCI6ImFsaWNlQGdydWVzLmRhdGF3aXJlLmlvIiwibmJmIjoxNDU1ODU3MTY1LCJzdWIiOiJncnVlLWxvY2F0b3IifQ.5DFHluutzdQaAPP6rtaPw9g9z-IZ50JV6ZEI5Kga7io";

// ...then set up Datawire Connect itself.
var datawire_connect = require('datawire_connect_1_0_0').datawire_connect;
var DWCResolver = datawire_connect.resolver.DiscoveryConsumer;

var datawire_discovery = require('discovery_1_0_0').datawire_discovery;
var DWCOptions = datawire_discovery.client.GatewayOptions;

var options = new DWCOptions(token);
options.gatewayHost = 'disco.datawire.io';

// OK. Fire up our Hello Datawire Connect client...
var client = new hello.HelloClient("hello");

// ...and point it to the correct resolver.
client.setResolver(new DWCResolver(options));

function makeACall (count) {
	var request = new hello.Request();

	request.text = "browser! [" + count + "]";

	var response = client.hello(request);

	response.onFinished({
		onFuture: function (response) {
            if (response.getError() !== null) {
                console.log("Response failed with", response.getError());
            } else {
                console.log("Response says", response.result);
            }
		}
	});

	setTimeout(function () {
		makeACall(count + 1);
	}, 1000);
}

