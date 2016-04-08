// JS Animated Server Example
/* jshint node: true */

"use strict";

var datawire_connect = require('datawire_connect').datawire_connect;
var DWCProvider = datawire_connect.resolver.DiscoveryProvider;

var datawire_discovery = require('discovery_1_0_0').datawire_discovery;
var DWCEndpoint = datawire_discovery.model.Endpoint;
var DWCOptions = datawire_discovery.client.GatewayOptions;

var token = require("token").token;

/******
 * Animated service handler
 */

var animated = require("animated").animated;

var AnimatedImpl = (function () {
  function AnimatedImpl(instance) {
    this.instance = instance;
  }

  AnimatedImpl.prototype.animated = function(request) {
    // The request has a color value and an octet to work with.
    // Start by splitting the color into three octets.
    var colors = [];
    colors[0] = (request.color >> 16) & 0xFF;
    colors[1] = (request.color >>  8) & 0xFF;
    colors[2] = (request.color      ) & 0xFF;

    // Increment the requested octet.
    var octet = request.octet;

    colors[octet] += 8;
    colors[octet] &= 0xFF;

    // Finally, reassemble the value.
    var response = new animated.Response();

    response.color = ((colors[0] << 16) |
                      (colors[1] << 8) |
                      (colors[2]));

    // Also record which instance we are.
    response.instance = this.instance;

    console.log("Instance " + response.instance + " for octet " + octet + ": " + response.color.toString(16).toUpperCase());

    var delay = 100 + (Math.random() * 500);

    if ((Math.random() * 3) < this.instance) {
      delay += 1000;
    }

    setTimeout(function() {
      response.finish(null); // XXX: response.finish() with no arg is a simple error to make and hard to debug as it's called with undefined :( should quark generate code to check required args?
    }, delay);

    return response;
  };

  return AnimatedImpl;
})();

/********
 * Datawire Connect stuff
 */

var ports = [ 8910, 8911, 8912 ];

for (var instance = 0; instance < ports.length; instance++) {
  var implementation = new AnimatedImpl(instance);
  var server = new animated.AnimatedServer(implementation);

  var port = ports[instance];

  var url = "http://127.0.0.1:" + port + "/";
  console.log("starting instance " + instance + " on " + url);

  server.serveHTTP(url);

  // OK. Our server is running, so register it with Datawire Connect.
  var endpoint = new DWCEndpoint('http', '127.0.0.1', port, url);
  var options = new DWCOptions(token);
  options.gatewayHost = "disco.datawire.io";

  var provider = new DWCProvider(options, "animated", endpoint);
  provider.register(15.0);

  console.log("registered server on " + url);
}

