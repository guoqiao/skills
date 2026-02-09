run:
	touch .env
	uv run --env-file .env bot.py

service:
	bash install_launchd_service.sh

tail:
	tail -f ~/Library/Logs/me.guoqiao.dlbot.log
