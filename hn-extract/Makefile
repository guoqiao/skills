name := hn-extract

m:
	uv run skill-metadata.py

M:
	uv run skill-metadata.py -v

hn_id ?= 46876105
out_dir ?= examples
example:
	mkdir -p ${out_dir}
	uv run --script ${name}/hn-extract.py ${hn_id} -o ${out_dir} -v

ex: example