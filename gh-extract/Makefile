slug := $(shell basename $(shell pwd))

m:
	@uv run skill-metadata.py --show

M:
	@uv run skill-metadata.py --show --verbose

publish:
	@uv run skill-metadata.py --publish

run := uv run --script ${slug}/${slug}.py
t:
	${run} https://github.com/guoqiao/skills
	${run} https://github.com/guoqiao/skills/tree/main/gh-extract/gh-extract
	${run} https://github.com/guoqiao/skills/blob/main/gh-extract/gh-extract/SKILL.md
