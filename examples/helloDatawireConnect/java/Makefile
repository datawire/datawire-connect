MAVENROOT=$(HOME)/.m2/repository

ifeq ($(MAVENROOT), /.m2)
    $(error WTF?
endif

all:
	@if [ ! -d '$(MAVENROOT)/hello/hello' ]; then \
		echo "You need to 'quark install hello.q' first!" >&2 ;\
		exit 1 ;\
	fi
	mvn compile

runserver:
	mvn exec:java -Dexec.mainClass=helloRPC.HelloRPCServer

runclient:
	mvn exec:java -Dexec.mainClass=helloRPC.HelloRPCClient

clean:
	mvn clean

clobber: clean
	-rm -rf '$(MAVENROOT)/hello'

