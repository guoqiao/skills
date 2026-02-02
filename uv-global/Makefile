name := uv-global

install:
	bash ${name}/uv-global.sh

i: install

metadata:
	uv run skill-metadata.py

m: metadata

tags:
	@echo "latest,python,uv,global,venv"

