slug := $(shell basename $(shell pwd))

install:
	bash ${slug}/install.sh

i: install

m:
	@uv run skill-metadata.py --show

M:
	@uv run skill-metadata.py --show --verbose

publish:
	@uv run skill-metadata.py --publish
