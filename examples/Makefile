all: d3 helloDatawireConnect market

.ALWAYS:

d3: .ALWAYS
	( cd d3 && $(MAKE) )

helloDatawireConnect: .ALWAYS
	( cd helloDatawireConnect && $(MAKE) )

market: .ALWAYS
	( cd market && $(MAKE) )

clean:
	@for dir in d3 helloDatawireConnect market; do \
		( cd $$dir && $(MAKE) clean ) ;\
	done

clobber:
	@for dir in d3 helloDatawireConnect market; do \
		( cd $$dir && $(MAKE) clobber ) ;\
	done
