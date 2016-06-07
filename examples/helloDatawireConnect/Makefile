CHECK=sh ../../checkenv/check.sh

all: \
	checkEnv node_modules quark-all \
	python-example node-example browser-example java-example

.ALWAYS:

install-dwc: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/datawire-cli/master/install.sh | bash -s -- -qq -t venv

install-quark: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/quark/master/install.sh | bash -s -- -qq

checkEnv: python-env node-env java-env
	$(CHECK) quark dwc hello-token

token: .ALWAYS
	dwc create-service hello

python-env:
	$(CHECK) pip

npm-env:
	$(CHECK) npm

node-env: npm-env

browser-env: npm-env

java-env:
	$(CHECK) mvn

node_modules:
	mkdir node_modules

quark-all: node_modules
	quark install --python --javascript --java hello.q

python-example:
	cd python && $(MAKE) example

node-example:
	cd node && $(MAKE) example

browser-example:
	cd browser && $(MAKE) example

java-example:
	cd java && $(MAKE) example

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
