all: node_modules
	quark install hello.q
	cd python && $(MAKE)
	cd node && $(MAKE)
	cd browser && $(MAKE)

python: .ALWAYS
	quark install --python hello.q
	cd python && $(MAKE)

node javascript: node_modules .ALWAYS
	quark install --javascript hello.q
	cd node && $(MAKE)

browser: node_modules .ALWAYS
	quark install --javascript hello.q
	cd browser && $(MAKE)

node_modules:
	mkdir node_modules

java: .ALWAYS
	quark install --java hello.q
	cd java && $(MAKE)

javaserver java-server: .ALWAYS
	cd java && $(MAKE) runserver

javaclient java-client: .ALWAYS
	cd java && $(MAKE) runclient

.ALWAYS:

clean:
	cd node && $(MAKE) clean
	cd browser && $(MAKE) clean
	cd python && $(MAKE) clean
	cd java && $(MAKE) clean

clobber: clean
	cd node && $(MAKE) clobber
	cd browser && $(MAKE) clobber
	cd python && $(MAKE) clobber
	cd java && $(MAKE) clobber
	rm -rf node_modules
