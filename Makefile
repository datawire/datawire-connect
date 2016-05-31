VERSION=$(shell cat VERSION)

all: examples

.ALWAYS:

checkEnv:
	@which dwc >/dev/null 2>&1 || { \
		echo "Could not find dwc -- is it installed?" >&2 ;\
		echo "" >&2 ;\
		cat README-DWC.txt >&2 ;\
		exit 1 ;\
	}
	@which quark >/dev/null 2>&1 || { \
		echo "Could not find quark -- is it installed?" >&2 ;\
		echo "" >&2 ;\
		cat README-QUARK.txt >&2 ;\
		exit 1 ;\
	}

install-dwc: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/datawire-cli/master/install.sh | bash -s -- -qq -t venv

install-quark: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/quark/master/install.sh | bash -s -- -qq

examples: checkEnv .ALWAYS
	( cd examples && $(MAKE) )

clean:
	-find . -iname '*.pyc' -print0 | xargs -0 rm -f
	-find . -iname '*.qc' -print0 | xargs -0 rm -f
	
clobber: clean
	# Empty node_modules, but don't delete it (it has a .gitignore)
	# -rm -rf node_modules/*
