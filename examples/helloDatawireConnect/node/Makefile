all:
	@echo "You should be running 'make node' from one directory up."

NPMROOT=$(shell npm root)

ifeq ($(NPMROOT), )
    $(error Can't find an npm root -- check whether npm is installed)
endif

# There's nothing to do for Node except the NPM check, which is kind of nice.
example:

clean:

clobber: clean
