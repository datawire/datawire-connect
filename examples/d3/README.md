Browser test
============

This uses Datawire Connect with cloud discovery to make a bunch of RPC calls from the browser, while also doing a bunch of (not-at-all optimized) animations asynchronously to the RPCs.

To try this, you'll need to install Quark and Datawire Cloud Tools (we recommend using virtualenv for this):

        pip install 'datawire-quark>=0.4.16'`
        pip install datawire-cloudtools

Once the Cloud Tools are installed, you'll need a Datawire Connect organization and service token. If you already have an organization set up, great, you can use that. If not, 

        dwc create-org

will tell you how to create an organization.

Given an organization, you'll create a service token for a service called 'animated':

        dwc create-service animated

Once that's done, you can get everything else set up by simply running make:
        
        make

Next, start the webserver running, since browsers typically want to be talking HTTP to actually execute JavaScript:

        make webserver

Then, in a separate window, start the RPC server that provides the service that the test wants:

        make rpcserver

Finally, open `http://localhost:8000/d3.html` in a web browser.

Also note that there is a stripped-down command-line client in `animCLI.js`. To see it, start the RPC server and then run

        node animCLI.js

The browser and the CLI version can both run simultaneously.

_NOTE WELL_: This has only been tested with Chrome right now.
