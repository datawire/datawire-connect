var datawire_connect = require('datawire_connect').datawire_connect;
var DWCResolver = datawire_connect.resolver.DiscoveryConsumer;

var datawire_discovery = require('discovery_1_0_0').datawire_discovery;
var DWCOptions = datawire_discovery.client.GatewayOptions;

// Snare the "Animated" service contract...
var animated = require("animated").animated;
var token = require("token").token;

console.log("token: " + token);

// /********
//  * GLOBALS
//  *
//  * We keep track of three colors and three latencies. VERY IMPORTANT: the indices don't
//  * mean the same thing. 
//  *
//  * colors[] is indexed by the octet we're asking about.
//  * latencies[] is indexed by the service instance that answered us.
//  */

var colors = [ 0x800000, 0x008000, 0x4444EE ];
var latencies = [ 0, 0, 0 ];
var avgLatencies = [ 0, 0, 0 ];
var numBoxCars = 10.0;

/********
 * TIMER
 */

var millitime = function () {
  return +new Date();
}

if (typeof(performance) != 'undefined') {
  millitime = function () {
    return Math.floor(performance.now());
  }
}

/********
 * LATENCIES
 */

function trackLatency(instance, latency) {
  latencies[instance] = latency;

  avg = avgLatencies[instance]

  avg = ((avg * (numBoxCars - 1)) + latency) / numBoxCars;

  avgLatencies[instance] = avg;
}

/********
 * HEX FORMATTING
 */

var hexFmt = d3.format('06X');
var floatFmt = d3.format('0.2f');

/********
 * COLOR REQUEST
 *
 * Here we're calling out to our microservice that cycles over colors for us.
 */

var callsEnabled = false;

function makeACall (client, octet) {
  var request = new animated.Request();
  request.color = colors[octet];
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
        colors[octet] = response.color;
        trackLatency(response.instance, elapsed);

        logStr += " got color " + hexFmt(colors[octet]) + " from instance " + response.instance;
      }

      console.log(logStr);

      if (callsEnabled) {
        setTimeout(function () {
          makeACall(client, octet);
        }, 1000);
      }
    }
  });
}

/********
 * Datawire Connect setup
 */

var options = new DWCOptions(token);
options.gatewayHost = 'disco.datawire.io';

// OK. Fire up our Hello Datawire Connect client...
var client = new animated.AnimatedClient("animated");

// ...and point it to the correct resolver.
client.setResolver(new DWCResolver(options));

function makeAllCalls() {
  if (!callsEnabled) {
    callsEnabled = true;
    makeACall(client, 0);
    makeACall(client, 1);
    makeACall(client, 2);   
  }
}

function stopAllCalls() {
  callsEnabled = false;
}

/********
 * D3
 */

/* Here's a buncha stuff for the ticking pie chart. */
var pieSlices = [1, 2, 3];

var width = 500,
    height = 500,
    outerRadius = height / 2 - 30,
    cornerRadius = 20;

var pie = d3.layout.pie();

var arc = d3.svg.arc()
          .outerRadius(outerRadius);

var pieSVG = 
  d3.select("#arc-div").append("svg")
    .attr("width", width)
    .attr("height", height)
    .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
    ;

var straightPath = 
  pieSVG.append("g")
        .attr("class", "paths--straight")
        .selectAll("path")
        .data(pieSlices)
        .enter()
        .append("path");

var roundPath =
  pieSVG.append("g")
        .attr("class", "paths--round")
        .selectAll("path")
        .data(pieSlices)
        .enter()
        .append("path");

var ease = d3.ease("cubic-in-out");
var duration = 5000;

d3.timer(function(elapsed) {
  // console.log("------");
  var t = ease(1 - Math.abs((elapsed % duration) / duration - .5) * 2);
  // var arcs = pie.padAngle(t * .1)(pieSlices);
  var arcs = pie.padAngle(.1)(pieSlices);

  var startAngle = t * (Math.PI / 2);
  pie.startAngle(startAngle);
  pie.endAngle(startAngle + (2 * Math.PI));

  // arc.innerRadius(outerRadius / (3 - t));
  arc.innerRadius(outerRadius / 4);
  straightPath.data(arcs).attr("d", arc.cornerRadius(0));
  roundPath.data(arcs)
    .attr("d", arc.cornerRadius(cornerRadius * (t + 1)))
    .attr("fill", function (d) {
      var arcNum = d.value - 1;
      var col = '#' + hexFmt(colors[arcNum]);
      // console.log("fill " + arcNum + " => " + col);

      return col;
    });
});

/* Here's a buncha stuff for the latency bar charts. */

function graphLatency(divID, arrayName, fillColor) {
  var barWidth = 420,
      barHeight = 20;

  var tracked = window[arrayName];

  var x = d3.scale.linear()
      .domain([0, d3.max(tracked)])
      .range([0, width]);

  var chartSVG =
    d3.select(divID).append("svg")
      .attr("width", barWidth)
      .attr("height", barHeight * tracked.length);

  var barChart =
    chartSVG.selectAll("g")
            .data(tracked)
            .enter().append("g")
            .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

  barChart.append("rect")
          .attr("width", x)
          .attr("height", barHeight - 1)
          .style("fill", fillColor);

  barChart.append("text")
          .attr("x", 0)
          .attr("y", barHeight / 2)
          .attr("dy", ".35em")
          .style("fill", "white")
          .text(function(d) { return floatFmt(d); });

  d3.timer(function(elapsed) {
    var x = d3.scale.linear()
        .domain([0, d3.max(tracked)])
        .range([0, width]);

    chartSVG.selectAll('rect').data(tracked).attr('width', x);
    chartSVG.selectAll('text').data(tracked).text(function(d) { return(floatFmt(d)); });
  });
}

graphLatency('#dash-div', 'latencies', '#FF0000');
graphLatency('#avg-div', 'avgLatencies', '#888888');

/* Here's a buncha stuff for showing the current colors */

function graphColors() {
  for (var i = 0; i < colors.length; i++) {
    var divNum = i + 1;
    var col = '#' + hexFmt(colors[i]);

    document.getElementById('label' + divNum).innerHTML = col;
    document.getElementById('color' + divNum).style.backgroundColor = col;
  }
}

graphColors();
d3.timer(function (elapsed) { graphColors(); });
