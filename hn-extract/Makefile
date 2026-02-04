name := hn-extract

m:
	uv run skill-metadata.py

M:
	uv run skill-metadata.py -v

hn_id ?= 46881264
out_dir ?= examples
example:
	mkdir -p ${out_dir}
	uv run --script ${name}/hn-extract.py ${hn_id} -o ${out_dir}/hn-${hn_id}.md -j ${out_dir}/hn-${hn_id}.json

ex: example