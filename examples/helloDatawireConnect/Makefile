all: \
	checkEnv node_modules quark-all \
	python-example node-example browser-example java-example

.ALWAYS:

checkEnv: python-env node-env java-env
	@which quark >/dev/null 2>&1 || { \
		echo "Could not find quark -- is it installed?" >&2 ;\
		echo "" >&2 ;\
		cat README-QUARK.txt >&2 ;\
		exit 1 ;\
	}
	@which dwc >/dev/null 2>&1 || { \
		echo "Could not find dwc -- is it installed?" >&2 ;\
		echo "" >&2 ;\
		cat README-DWC.txt >&2 ;\
		exit 1 ;\
	}
	@dwc service-token hello >/dev/null 2>&1 || { \
		echo "Could not find token for the hello service -- did you create one?" >&2 ;\
		echo "" >&2 ;\
		cat README-TOKEN.txt >&2 ;\
		exit 1 ;\
 	}

token: .ALWAYS
	dwc create-service hello

python-env:
	@which pip >/dev/null 2>&1 || { \
		echo "Could not find pip -- should you be in a virtualenv?" >&2 ;\
		echo "" >&2 ;\
		cat README-PIP.txt >&2 ;\
		exit 1 ;\
	}

npm-env:
	@which npm >/dev/null 2>&1 || { \
		echo "Could not find npm -- is it installed?" >&2 ;\
		echo "" >&2 ;\
		cat README-NPM.txt >&2 ;\
		exit 1 ;\
	}

node-env: npm-env

browser-env: npm-env

java-env:
	@which mvn >/dev/null 2>&1 || { \
		echo "Could not find mvn -- is it installed?" >&2 ;\
		echo "" >&2 ;\
		cat README-MVN.txt >&2 ;\
		exit 1 ;\
	}
	@mvn -v >/dev/null 2>&1 || { \
		echo "mvn doesn't seem to run correctly -- try mvn -v?" >&2 ;\
		echo "" >&2 ;\
		cat README-MVN.txt >&2 ;\
		exit 1 ;\
	}

node_modules:
	mkdir node_modules

quark-all: node_modules
	quark install --python --javascript --java hello.q

python-example:
	cd python && $(MAKE)

node-example:
	cd node && $(MAKE)

browser-example:
	cd browser && $(MAKE)

java-example:
	cd java && $(MAKE)

python: .ALWAYS
	quark install --python hello.q
	$(MAKE) python-example

node javascript: node_modules .ALWAYS
	quark install --javascript hello.q
	$(MAKE) node-example

browser: node_modules .ALWAYS
	quark install --javascript hello.q
	$(MAKE) browser-example

java: .ALWAYS
	quark install --java hello.q
	$(MAKE) java-example

javaserver java-server: .ALWAYS
	cd java && $(MAKE) runserver

javaclient java-client: .ALWAYS
	cd java && $(MAKE) runclient

clean-toplevel:
	-rm -f hello.qc

clean: clean-toplevel
	cd node && $(MAKE) clean
	cd browser && $(MAKE) clean
	cd python && $(MAKE) clean
	cd java && $(MAKE) clean

# clobber relies on subdirectory clobber doing a clean as well.
clobber: clean-toplevel
	cd node && $(MAKE) clobber
	cd browser && $(MAKE) clobber
	cd python && $(MAKE) clobber
	cd java && $(MAKE) clobber
	rm -rf node_modules
