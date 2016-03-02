Browser test
============

This uses Datawire Connect with cloud discovery to make a bunch of RPC calls from the browser, while also doing a bunch of (not-at-all optimized) animations asynchronously to the RPCs.

The simplest way to try it out is to start by bootstrapping the world in a totally clean directory. Here's the simplest way to do it:

        mkdir new_dir
        cd new_dir
        
        virtualenv test
        . test/bin/activate
        
        git clone git@github.com:datawire/quark
        cd quark
        git checkout flynn/feature/evilBrowserSupport
        python setup.py develop
        cd ..
        
        git clone git@github.com:datawire/datawire-connect
        cd datawire-connect
        git checkout flynn/feature/evilBrowserSupport
        cd examples/browser/d3
        
        make

Next, start the webserver running, since browsers typically want to be talking HTTP to actually execute JavaScript:

        make webserver

Then, in a separate window, start the RPC server that provides the service that the test wants:

        make rpcserver

Finally, open `http://localhost:8000/d3.html` in a web browser.

_NOTE WELL_: This has only been tested with Chrome right now.
