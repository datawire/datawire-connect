Browser test
============

This uses Datawire Connect with cloud discovery to make a bunch of RPC calls from the browser, while also doing a bunch of (not-at-all optimized) animations asynchronously to the RPCs.

To try it out:

0. _Note well_: if you're here, you cloned `datawire-connect`.
   - You'll need to also clone `datawire-quark`, and check out the `flynn/feature/evilBrowserSupport` branch there.
   - Your `datawire-quark` clone must be a sibling of this `datawire-connect` clone, so that `../../../../quark` reaches it.

1. `make`

This will pull in all the relevant NPM modules, etc., and get everything set up.

2. `make webserver`

This will start a local webserver running, since browsers typically want to be talking HTTP to actually execute JavaScript.

3. In a separate window, `make rpcserver`

This will start a (JavaScript, at present) RPC server to provide the service that the test wants.

4. Open `http://localhost:8000/d3.html` in a web browser.

This has only been tested with Chrome right now.
