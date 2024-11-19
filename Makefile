all:
	- rm python/*
	- rm ts/*
	- rm LICENSE.txt
	cd ../py-job-runner && \
		pip-licenses --with-license-file --format=json > third-party-licenses-py-job-runner.json && \
		mv third-party-licenses-py-job-runner.json ../licenses/python/.
	cd ../search && \
		pip-licenses --with-license-file --format=json > third-party-licenses-search.json && \
		mv third-party-licenses-search.json ../licenses/python/.
	cd ../benchify-scraper && \
		pip-licenses --with-license-file --format=json > third-party-licenses-scraper.json && \
		mv third-party-licenses-scraper.json ../licenses/python/.
	cd ../ts-job-runner && \
		license-checker --json > third-party-licenses-ts-job-runner.json && \
		mv third-party-licenses-ts-job-runner.json ../licenses/ts/.
	cd ../benchify-github && \
		license-checker --json > third-party-licenses-benchify-github.json && \
		mv third-party-licenses-benchify-github.json ../licenses/ts/.
	python3 makeLicense.py

deps:
	pip install pip-licenses
	npm install -g license-checker