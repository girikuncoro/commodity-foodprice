clean:
	rm -rf venv/

venv:
	virtualenv venv

install: clean venv
	source ./venv/bin/activate; \
	pip install -r requirements.txt;

heroku-local:
	source ./venv/bin/activate; \
	heroku local; \
