// animCLI.js is a stripped-down sample of how you can call a Datawire Connect
// service from JavaScript. Run with 'node animCLI.js' and it'll make one call
// every second.

var datawire_connect = require('datawire_connect').datawire_connect;
var DWCResolver = datawire_connect.resolver.DiscoveryConsumer;

var datawire_discovery = require('discovery_1_0_0').datawire_discovery;
var DWCOptions = datawire_discovery.client.GatewayOptions;

// Snare the "Animated" service contract...
var animated = require("animated").animated;

// ...and our token.
var token = require("token").token;

/********
 * Actual client
 */

var millitime = function () {
  return +new Date();
}

if (typeof(performance) != 'undefined') {
  millitime = function () {
    return Math.floor(performance.now());
  }
}

var color = 0x000000;

function makeACall (client, octet) {
  var request = new animated.Request();
  request.color = color;
  request.octet = octet;

  var start = millitime();
  var response = client.animated(request);

  response.onFinished({
    onFuture: function (response) {
      var finished = millitime();
      var elapsed = finished - start;

      var logStr = "OCT " + octet + " (" + elapsed + " ms):";

      if (response.getError() !== null) {
        logStr += " failed: " + response.getError();
      }
      else {
        color = response.color;
        logStr += " got color " + color.toString(16).toUpperCase() + " from instance " + response.instance;
      }

      console.log(logStr);

      setTimeout(function () {
        makeACall(client, octet);
      }, 1000);
    }
  });
}

// Set up Datawire Connect itself.
var options = new DWCOptions(token);
options.gatewayHost = 'disco.datawire.io';

// OK. Fire up our Hello Datawire Connect client...
var client = new animated.AnimatedClient("animated");

// ...point it to the correct resolver...
client.setResolver(new DWCResolver(options));

// ...and start the first call.
setTimeout(function () {
  makeACall(client, 0);
}, 1000);
