slug := $(shell basename $(shell pwd))

m:
	@uv run skill-metadata.py --show

M:
	@uv run skill-metadata.py --show --verbose

publish:
	@uv run skill-metadata.py --publish
