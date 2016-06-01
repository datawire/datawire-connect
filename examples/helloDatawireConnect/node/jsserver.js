// JS Hello Server Example
/* jshint node: true */

"use strict";

var util = require('util');

var datawire_connect = require('datawire_connect').datawire_connect;
var DatawireState = datawire_connect.state.DatawireState;
var DWCProvider = datawire_connect.resolver.DiscoveryProvider;

var datawire_discovery = require('discovery_1_0_0').datawire_discovery;
var DWCEndpoint = datawire_discovery.model.Endpoint;
var DWCOptions = datawire_discovery.client.GatewayOptions;

// Start by grabbing our service contract and its token.
var hello = require("hello").hello;

/******** SERVICE IMPLEMENTATION ********/
var HelloImpl = (function () {
    function HelloImpl() {}

    util.inherits(HelloImpl, hello.Hello);

    HelloImpl.prototype.hello = function (request) {
        // Say hello!

        // Snare a response object...
        var response = new hello.Response();

        // ...and fill it in.
        response.result = "Responding to [" + request.text + "] from JavaScript";

        var delay = 0;
        // Uncomment the next line to simulate a long request processing
        // time (which may cause a timeout for the client, of course).
        // delay = 5000;

        setTimeout(function() {
            // Mark our response as finished, so that when our caller gets
            // it, they know that everything that needs doing is done.
            response.finish(null);
        }, delay);

        return response;
    };

    return HelloImpl;
})();

/******** MAINLINE ********/

// Grab our service token.
var dwState = DatawireState.defaultState();
var token = dwState.getCurrentServiceToken("hello");

// Start our server running...
var url = "http://127.0.0.1:8910/"

var implementation = new HelloImpl();
var server = new hello.HelloServer(implementation);
server.sendCORS(true);
server.serveHTTP(url);

// ...and then register it with Datawire Connect.
var endpoint = new DWCEndpoint('http', '127.0.0.1', 8910, url);
var options = new DWCOptions(token);

var provider = new DWCProvider(options, "hello", endpoint);
provider.register(15.0);

console.log("registered JavaScript server on " + url);
