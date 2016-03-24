NPMROOT=$(shell npm root)

ifeq ($(NPMROOT), )
    $(error Can't find an npm root -- check whether npm is installed)
endif

all: token

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

clean:

clobber: clean
	-rm -f '$(NPMROOT)/token.js'
