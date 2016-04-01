// JS Hello Server Example
/* jshint node: true */

"use strict";

var datawire_connect = require('datawire_connect_1_0_0').datawire_connect;
var DatawireState = datawire_connect.state.DatawireState;
var DWCProvider = datawire_connect.resolver.DiscoveryProvider;

var datawire_discovery = require('discovery_1_0_0').datawire_discovery;
var DWCEndpoint = datawire_discovery.model.Endpoint;
var DWCOptions = datawire_discovery.client.GatewayOptions;

// Start by grabbing our service contract and its token.
var hello = require("hello").hello;

var dwState = DatawireState.defaultState();
var token = dwState.getCurrentServiceToken("hello");

var HelloImpl = (function () {
    function HelloImpl() {}

    HelloImpl.prototype.hello = function (request) {
        var response = new hello.Response();
        response.result = "Responding to [" + request.text + "] from JavaScript";

        var delay = 0;
        // Uncomment the next line to simulate a long request processing
        // time and force a request timeout to occur for the client.
        // delay = 5000;

        setTimeout(function() {
            response.finish(null); // XXX: response.finish() with no arg is a simple error to make and hard to debug as it's called with undefined :( should quark generate code to check required args?
        }, delay);

        return response;
    };

    return HelloImpl;
})();

var implementation = new HelloImpl();
var server = new hello.HelloServer(implementation);

var ports = [ 8910, 8911, 8912 ];

for (var i = ports.length - 1; i >= 0; i--) {
    var port = ports[i];

    var url = "http://127.0.0.1:" + port + "/";
    console.log("starting server on " + url);

    server.serveHTTP(url);

    // OK. Our server is running, so register it with Datawire Connect.
    var endpoint = new DWCEndpoint('http', '127.0.0.1', port, url);
    var options = new DWCOptions(token);

    var provider = new DWCProvider(options, "hello", endpoint);
    provider.register(15.0);

    console.log("registered server on " + url);
}

