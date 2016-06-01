CHECK=sh ../../../checkenv/check.sh

all: checkVirtual checkEnv prep ratingsService start

checkVirtual:
	@if [ -z "$$VIRTUAL_ENV" ]; then \
		echo "Please activate a virtualenv to continue (cf https://virtualenv.readthedocs.org)" >&2 ;\
		exit 1; \
	fi

checkEnv:
	$(CHECK) quark dwc pip ratings-token

install-dwc: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/datawire-cli/master/install.sh | bash -s -- -qq -t venv

install-quark: .ALWAYS
	curl -# -L https://raw.githubusercontent.com/datawire/quark/master/install.sh | bash -s -- -qq

prep:
	pip install -r requirements.txt

ratingsService:
	quark install --python ../ratings/ratings.q

start:
	python market.py

test tests:
	@echo "Make sure the Market is running, then Y to continue or N to quit:"
	@read junk ;\
	case $$junk in \
	  y|Y)  nosetests ;\
            ;; \
      *)    ;; \
    esac
