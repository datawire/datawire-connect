NPMROOT=$(shell npm root)

ifeq ($(NPMROOT), )
    $(error Can't find an npm root -- check whether npm is installed)
endif

all: browser

browser: npm bhello-min.js

npm:
	npm -q install browserify uglifyjs

token:
	@echo grabbing service token
	@eval $$(dwc service-token hello | sed -e's/ //g') ;\
	\
	if [ -n "$$svc_token" ]; then \
		echo "module.exports = { token: '$$svc_token' };" > '$(NPMROOT)/token.js' ;\
		exit 0 ;\
	else \
		echo "no 'hello' token??" >&2 ;\
		exit 1 ;\
	fi

bhello-min.js: token
	'$(NPMROOT)/.bin/browserify' -d -o bhello.js \
		-x ws \
		-r quark \
		-r quark/quark_node_runtime \
		-r discovery_1_0_0 \
		-r datawire_connect \
		-r hello \
		-r token
	'$(NPMROOT)/.bin/uglifyjs' \
		--mangle --compress --stats -o bhello-min.js bhello.js 2>&1 \
	   | fgrep -v 'Dropping unused' \
	   | fgrep -v 'Side effects in initialization of unused variable' \
	   | fgrep -v 'Dropping unreachable code' \
	   | fgrep -v 'Declarations in unreachable code' \
	   | fgrep -v 'Condition always false'

clean:
	-rm -f bhello.js bhello-min.js

clobber: clean
	-rm -f '$(NPMROOT)/token.js'
