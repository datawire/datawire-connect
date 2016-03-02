all: npm animated

node_modules:
	mkdir node_modules

npm: node_modules
	npm install request browserify uglifyjs

animated:
	quark install --javascript animated.q
	cp ../../../../quark/quarkc/builtin/quark_*runtime.js node_modules/builtin
	node_modules/.bin/browserify -d -o bquark.js \
		-r builtin \
		-r discovery_1_0_0 \
		-r datawire_connect_1_0_0 \
		-r builtin/quark_browser_runtime.js \
		-r animated
	node_modules/.bin/uglifyjs --mangle --compress --stats -o bquark-min.js bquark.js

clean:
	-rm -f bquark.js bquark-min.js

clobber: clean
	-rm -rf node_modules

webserver:
	python -m SimpleHTTPServer

rpcserver:
	node jsserver.js

