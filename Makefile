clean:
	rm -rf venv/

venv:
	virtualenv venv

install: clean venv
	source ./venv/bin/activate; \
	pip install -r requirements.txt;

serve:
	source ./venv/bin/activate; \
	python app/main.py; \
