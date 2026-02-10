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

undelete:
	clawhub undelete ${slug}


url1 := https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
t1:
	uv run --script ${slug}/${slug}.py ${url1}

url2 := https://www.ruanyifeng.com/blog/2026/01/weekly-issue-383.html
t2:
	uv run --script ${slug}/${slug}.py ${url2}
