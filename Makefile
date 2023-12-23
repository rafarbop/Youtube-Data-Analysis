SHELL := /bin/bash

venv:
	python -m venv venv

install:
	pip install -U pip
	pip install -r requirements.txt

clean:
	rm -r venv
	rm -r report

test:
	coverage run -m pytest -v
	coverage report
	coverage html

docker-build:
	docker build --file Dockerfile.local -t youtube-data-analysis .

docker-run:
	docker run -p 8000:8000 youtube-data-analysis:latest uvicorn --host 0.0.0.0  run:create_app
