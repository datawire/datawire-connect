CHECK=sh ../../checkenv/check.sh

all: checkEnv npm animated

checkEnv:
	$(CHECK) quark dwc npm animated-token

install-dwc: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/datawire-cli/master/install.sh | bash -s -- -qq -t venv

install-quark: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/quark/master/install.sh | bash -s -- -qq

node_modules:
	mkdir node_modules

npm: node_modules
	npm -q install browserify uglifyjs

token: node_modules
	@echo grabbing service token
	@eval $$(dwc service-token animated | sed -e's/ //g') ;\
	\
	if [ -n "$$svc_token" ]; then \
		echo "module.exports = { token: '$$svc_token' };" > node_modules/token.js ;\
		exit 0 ;\
	else \
		echo "no 'animated' token??" >&2 ;\
		exit 1 ;\
	fi

animated: token
	quark install --javascript animated.q
	node_modules/.bin/browserify -d -o bquark.js \
		-x ws \
		-r quark \
		-r discovery_1_0_0 \
		-r datawire_connect \
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
	-rm -rf *.qc

webserver:
	python -m SimpleHTTPServer

rpcserver:
	node jsserver.js
