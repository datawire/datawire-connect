all:
	quark install hello.q
	cd node && $(MAKE)
	cd browser && $(MAKE)

node javascript: node_modules .ALWAYS
	quark install --javascript hello.q
	cd node && $(MAKE)

browser: node_modules .ALWAYS
	quark install --javascript hello.q
	cd browser && $(MAKE)

node_modules:
	mkdir node_modules

.ALWAYS:

clean:
	cd node && $(MAKE) clean
	cd browser && $(MAKE) clean

clobber: clean
	cd node && $(MAKE) clobber
	cd browser && $(MAKE) clobber
	rm -rf node_modules
