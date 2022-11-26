site: data/* jinja/* venv
	;
venv: pyproject.toml
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
