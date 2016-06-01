VERSION=$(shell cat VERSION)

CHECK=sh checkenv/check.sh

all: examples

.ALWAYS:

checkEnv:
	$(CHECK) dwc quark

install-dwc: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/datawire-cli/master/install.sh | bash -s -- -qq -t venv

install-quark: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/quark/master/install.sh | bash -s -- -qq

examples: checkEnv .ALWAYS
	( cd examples && $(MAKE) )

clean:
	( cd examples && $(MAKE) clean)
	-find . -iname '*.pyc' -print0 | xargs -0 rm -f
	-find . -iname '*.qc' -print0 | xargs -0 rm -f
	
clobber: clean
	( cd examples && $(MAKE) clobber)
