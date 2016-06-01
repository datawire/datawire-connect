#!/bin/sh

DIR=$(cd $(dirname "$0"); pwd)

checkwhich () {
	cmd="$1"
	readme="$2"
	question="$3"

	if [ -z "$question" ]; then
		question="is it installed"
	fi

	which "$cmd" >/dev/null 2>&1 || { \
		echo "Could not find ${cmd} -- ${question}?" >&2 ;\
		echo "" >&2 ;\
		cat "${DIR}/$readme" >&2 ;\
		exit 1 ;\
	}
}

checktoken () {
	svc="$1"

	checkwhich dwc README-DWC.txt

	dwc service-token "${svc}" >/dev/null 2>&1 || { \
		echo "Could not find token for the ${svc} service -- did you create one?" >&2 ;\
		echo "" >&2 ;\
		cat ${DIR}/README-TOKEN.txt >&2 ;\
		exit 1 ;\
 	}
}

checkmvn () {
	checkwhich mvn README-MVN.txt

	mvn -v >/dev/null 2>&1 || {
		echo "mvn doesn't seem to run correctly -- try mvn -v?" >&2 ;\
		echo "" >&2 ;\
		cat ${DIR}/README-MVN.txt >&2 ;\
		exit 1 ;\
	}
}

for arg in "$@"; do
	case "$arg" in
		dwc)	checkwhich dwc README-DWC.txt ;;
		quark)	checkwhich quark README-QUARK.txt ;;
		hello-token) checktoken hello;;
		animated-token) checktoken animated;;
		ratings-token) checktoken ratings;;
		pip)	checkwhich pip README-PIP.txt "should you be in a virtualenv";;
		npm)	checkwhich npm README-NPM.txt;;
		mvn)	checkmvn ;;
	esac
done	
