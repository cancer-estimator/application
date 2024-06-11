PROJECT_NAME = cancer-estimator-application
DOCKER_REGISTRY := ryukinix/$(PROJECT_NAME)
VERSION ?= latest
UID = $(shell id -u)
GID = $(shell id -g)
DOCKER_RUN = docker run $(DOCKER_FLAGS) \
					--user $(UID):$(GID) \
					-e HOME=/tmp --rm \
					-t \
                    -p 8000:8000 \
					-v $(PWD)/tests:/project/tests \
					-w /app

install: # install locally
	python -m venv .venv
	source .venv/bin/activate
	pip install -U pdm setuptools wheel
	pdm install

run: build
	$(DOCKER_RUN) $(PROJECT_NAME)

run-local:
	fastapi dev cancer_estimator_application/main.py

build:
	docker build -t $(PROJECT_NAME) .

build-test:
	docker build -t $(PROJECT_NAME):test --target test .

publish: build
	docker tag $(PROJECT_NAME) $(DOCKER_REGISTRY):$(VERSION)
	docker push $(DOCKER_REGISTRY):$(VERSION)

deploy: publish
	bash scripts/deploy.sh

check: build-test
	$(DOCKER_RUN) $(PROJECT_NAME):test check

.PHONY: build build-test run run-local check install
