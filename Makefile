.PHONY: build
build: chapters/* jinja/* venv
	rm site/*.html
	./venv/bin/python build.py
venv: requrements.txt
	python3 -m venv --clear venv
	./venv/bin/pip install -r requirements.txt
