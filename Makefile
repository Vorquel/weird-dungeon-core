.PHONY: build
build: chapters/* jinja/* venv
	rm site/*.html || true
	./venv/bin/python build.py
venv: requirements.txt
	python3 -m venv --clear venv
	./venv/bin/pip install -r requirements.txt
