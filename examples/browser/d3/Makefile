all: npm animated

node_modules:
	mkdir node_modules

npm: node_modules
	npm -q install browserify uglifyjs | grep '^[a-zA-Z0-9]'

animated:
	quark install --javascript animated.q
	node_modules/.bin/browserify -d -o bquark.js \
		-x ws \
		-r quark \
		-r discovery_1_0_0 \
		-r datawire_connect_1_0_0 \
		-r quark/quark_node_runtime\
		-r animated \
		-r token
	node_modules/.bin/uglifyjs \
		--mangle --compress --stats -o bquark-min.js bquark.js 2>&1 \
	   | fgrep -v 'Dropping unused' \
	   | fgrep -v 'Side effects in initialization of unused variable' \
	   | fgrep -v 'Dropping unreachable code' \
	   | fgrep -v 'Declarations in unreachable code' \
	   | fgrep -v 'Condition always false'

clean:
	-rm -f bquark.js bquark-min.js

clobber: clean
	-rm -rf node_modules

webserver:
	python -m SimpleHTTPServer

rpcserver:
	node jsserver.js

