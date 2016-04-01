VERSION=$(shell cat VERSION)

TESTGOLDFILE=$(shell echo /tmp/CloudTools-GOLD.$$PPID)

all: init quark test

.ALWAYS:

init:
	@if [ -z "$$VIRTUAL_ENV" ]; then echo "You must be in a venv for this"; false; fi
	pip install -r requirements.txt

quark: .ALWAYS
	quark install quark/datawire_connect-1.0.0.q

test: quark node_modules run-local-tests
	-rm -f $(TESTGOLDFILE)

run-local-tests:
	nosetests test
	python test/testDWState.py > $(TESTGOLDFILE)
	node test/testDWState.js $(TESTGOLDFILE)
	(cd test && mvn -q test -DGoldPath=$(TESTGOLDFILE))

clean:
	-find . -iname '*.pyc' -print0 | xargs -0 rm -f
	-rm -rf test/target
	
clobber: clean
	# Empty node_modules, but don't delete it (it has a .gitignore)
	-rm -rf node_modules/*
