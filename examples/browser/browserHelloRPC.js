var hello = require("hello").hello;

var client = new hello.HelloClient("http://localhost:8910/hello");

function FutureListener(cb) {
    this.onFuture = cb;
}

function makeACall (count) {
	var request = new hello.Request();

	request.text = "browser! [" + count + "]";

	var response = client.hello(request);

	response.onFinished(
	    new FutureListener( // XXX: if this can become magic then the quark-js API can be idiomatic
	        function(response) {
	            if (response.getError() !== null) {
	                console.log("Response failed with", response.getError());
	            } else {
	                console.log("Response says", response.result);
	            }
	        }));

	setTimeout(function () {
		makeACall(count + 1);
	}, 1000);
}

