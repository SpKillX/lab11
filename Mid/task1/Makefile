.PHONY: build test

build:
	docker build -t python-app-task1 .

test:
	pip install docker pytest requests
	pytest test_build.py