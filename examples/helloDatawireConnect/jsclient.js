// JS Hello Client Example
/* jshint node: true */

"use strict";
var process = require("process");
var hello = require("hello").hello;

var args = process.argv.splice(process.execArgv.length + 2);

if (args.length < 1) {
    throw "Usage: node jsserver.js service-token";
}

var token = args[0];

var text = "Hello from JavaScript";

if (args.length > 1) {
    text = args[1];
}

var hello = require("hello").hello;

var datawire_connect = require('datawire_connect_1_0_0').datawire_connect;
var DWCResolver = datawire_connect.resolver.DiscoveryConsumer;

var datawire_discovery = require('discovery_1_0_0').datawire_discovery;
var DWCOptions = datawire_discovery.client.GatewayOptions;

// "http://hello.datawire.io/" is the URL of the simple "Hello" cloud
// microservice run by Datawire, Inc. to serve as a simple first test.
//
//  You can test completely locally, too:
//  - comment out the http://hello.datawire.io line
//  - uncomment the http://127.0.0.1:8910/hello line
//  - fire up the local version of the server by following the instructions
//  in the README.md.
//
// var client = new hello.HelloClient("http://hello.datawire.io/");
// var client = new hello.HelloClient("http://localhost:8910/hello");

var options = new DWCOptions(token);
options.gatewayHost = 'disco.datawire.io';

var client = new hello.HelloClient("hello");
client.setResolver(new DWCResolver(options));

function sendRequest() {
    var request = new hello.Request();
    request.text = text;

    console.log("Request says", request.text);

    var response = client.hello(request);

    function FutureListener(cb) {
        this.onFuture = cb;
    }
    response.onFinished(
        new FutureListener( // XXX: if this can become magic then the quark-js API can be idiomatic
            function(response) {
                if (response.getError() !== null) {
                    console.log("Response failed with", response.getError());
                } else {
                    console.log("Response says", response.result);
                }
            }));
}

setTimeout(sendRequest, 5000);
