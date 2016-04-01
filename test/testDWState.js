var process = require('process');
var fs = require('fs');
var assert = require('assert');

var datawire_connect = require('datawire_connect_1_0_0').datawire_connect;
var DatawireState = datawire_connect.state.DatawireState;

var args = process.argv.splice(process.execArgv.length + 2);

var goldInfo = fs.readFileSync(args[0]).toString().split("\n");

var i = 0;

var goldDefaultPath = goldInfo[i++];
var goldOrgID = goldInfo[i++];
var goldEmail = goldInfo[i++];
var goldTokens = {};
var services = [];

while (i < goldInfo.length) {
	if (goldInfo[i].length > 0) {
		var tokenInfo = goldInfo[i].split(':::');

		var svcHandle = tokenInfo[0];
		var svcToken = tokenInfo[1];

		goldTokens[svcHandle] = svcToken;
		services.push(svcHandle);
	}

	i++;
}

var dwState = new DatawireState();

assert.equal(dwState.defaultStatePath(), goldDefaultPath);

dwState = DatawireState.defaultState();

assert.equal(dwState.getCurrentOrgID(), goldOrgID);
assert.equal(dwState.getCurrentEmail(), goldEmail);

var delSvc = [];

for (var i = 0; i < services.length; i++) {
	var svcHandle = services[i];
	var svcToken = dwState.getCurrentServiceToken(svcHandle);

	assert.equal(svcToken, goldTokens[svcHandle]);
	delSvc.push(svcHandle);
}

for (var i = 0; i < delSvc.length; i++) {
	delete(goldTokens[delSvc[i]]);
}

assert.equal(Object.keys(goldTokens).length, 0);
