all: monolith

.always:

monolith: .always
	cd monolith && make 

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
