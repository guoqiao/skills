service_id := me.guqiao.dlbot
domain_target := gui/$(shell id -u)
service_target := ${domain_target}/${service_id}
service_path := ${HOME}/Library/LaunchAgent/${service_id}.plist
log_path := ${HOME}/Library/Logs/${service_id}.log

run:
	touch .env
	uv run --env-file .env bot.py

service:
	bash install_launchd_service.sh

start:
	launchctl $@ --user ${service_target} || true

stop:
	launchctl $@ --user ${service_target} || true

bootstrap:
	launchctl bootstrap --user ${domain_target} ${service_path}

bootout:
	launchctl bootout --user ${service_target}

tail:
	tail -f ${log_path}
