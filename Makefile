venv:
	virtualenv venv
	source venv/bin/activate.fish

install:
	pip install -r requirements.txt
