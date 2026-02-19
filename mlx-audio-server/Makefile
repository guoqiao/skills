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


service := mlx-audio-server

info:
	brew services $@ ${service}

run:
	# run in foreground
	brew services $@ ${service}

start:
	brew services $@ ${service}

restart:
	brew services $@ ${service}

stop:
	brew services $@ ${service}

kill:
	brew services $@ ${service}

edit:
	vim ~/Library/LaunchAgents/me.guoqiao.mlx-audio-server.plist

tail:
	tail -n50 -f /opt/homebrew/var/log/mlx-audio-server/server.log
