slug := $(shell basename $(shell pwd))

m:
	@uv run skill-metadata.py --show

M:
	@uv run skill-metadata.py --show --verbose

publish:
	@uv run skill-metadata.py --publish

hn_id ?= 46876105
out_dir ?= examples
example:
	mkdir -p ${out_dir}
	uv run --script ${slug}/hn-extract.py ${hn_id} -o ${out_dir} -v

ex: example