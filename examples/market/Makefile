CHECK=sh ../../checkenv/check.sh

all: monolith

.always:

monolith: .always
	cd monolith && make 

datawire-connect: checkVirtual
	$(CHECK) dwc

install-dwc: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/datawire-cli/master/install.sh | bash -s -- -qq -t venv

install-quark: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/quark/master/install.sh | bash -s -- -qq

checkVirtual:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Please activate a virtualenv to continue (cf https://virtualenv.readthedocs.org)" >&2 ;\
		exit 1; \
	fi

add-ratings: .always
	cd add-ratings && make

add-prices: .always
	cd add-prices && make

# You can set INSTANCE, PORT, or COUNT when doing 'make startRatings'.
#
# With none, the server listens on port 8001 (instance 1).
#
# With PORT, the server listens on that specific port.
# With INSTANCE, the server listens on port 8000 + INSTANCE.
# With COUNT, the server listens on COUNT ports starting with 8001. 

startRatings:
	@iarg=""; parg=""; carg=""; \
	if [ -n "$$INSTANCE" ]; then iarg="--instance $$INSTANCE"; fi ;\
	if [ -n "$$PORT"     ]; then parg="--port $$PORT";         fi ;\
	if [ -n "$$COUNT"    ]; then carg="--count $$COUNT";       fi ;\
	\
	python ratings/ratingsService.py $$iarg $$parg $$carg

clean:

clobber:
