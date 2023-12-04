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
