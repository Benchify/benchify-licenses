deps:
	pip install pip-licenses
	npm install -g license-checker

all:
	cd ../py-job-runner && \
		pip-licenses --with-license-file --format=json > third-party-licenses-py-job-runner.json && \
		mv third-party-licenses-py-job-runner.json ../licenses/.
	cd ../ts-job-runner && \
		license-checker --json > third-party-licenses-ts-job-runner.json && \
		mv third-party-licenses-ts-job-runner.json ../licenses/.
	cd ../benchify-github && \
		license-checker --json > third-party-licenses-benchify-github.json && \
		mv third-party-licenses-benchify-github.json ../licenses/.
	python3 makeLicense.py