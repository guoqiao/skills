FORMULA := mlx-audio-server
LOG_FILE := $(shell brew --prefix)/var/log/mlx-audio-server/server.log

TAP_USER := guoqiao
TAP_REPO := tap
TAP_NAME := $(TAP_USER)/$(TAP_REPO)
TAP_PATH := $(shell brew --repo)/Library/Taps/$(TAP_USER)/homebrew-$(TAP_REPO)
CURRENT_PATH := $(shell pwd)

# Default: list targets
help:
	@echo "Available targets:"
	@echo "  setup      - Link this repo as a local Homebrew tap"
	@echo "  install    - Install the formula (HEAD version)"
	@echo "  uninstall  - Uninstall the formula"
	@echo "  reinstall  - Uninstall and install"
	@echo "  service    - Start the background service"
	@echo "  stop       - Stop the background service"
	@echo "  restart    - Restart the background service"
	@echo "  log        - Tail the service logs"
	@echo "  test       - Run tests defined in the formula"
	@echo "  audit      - Audit the formula for Homebrew standards"
	@echo "  lint       - Check Ruby style/offenses"

setup:
	@mkdir -p $(dir $(TAP_PATH))
	@if [ -d "$(TAP_PATH)" ]; then \
		if [ "$$(readlink "$(TAP_PATH)")" != "$(CURRENT_PATH)" ]; then \
			echo "Warning: Tap $(TAP_NAME) exists but points elsewhere."; \
			echo "Current: $$(readlink "$(TAP_PATH)")"; \
			echo "Expected: $(CURRENT_PATH)"; \
			echo "Please run 'brew untap $(TAP_NAME)' and try again."; \
			exit 1; \
		else \
			echo "Tap $(TAP_NAME) is already linked to $(CURRENT_PATH)"; \
		fi \
	else \
		echo "Linking $(CURRENT_PATH) to $(TAP_PATH)"; \
		ln -s "$(CURRENT_PATH)" "$(TAP_PATH)"; \
	fi

install: setup
	# Try to install; if it fails (linkage warnings), check if it was actually installed
	brew install --HEAD $(TAP_NAME)/$(FORMULA) || brew list $(FORMULA)
	make service

uninstall:
	brew $@ $(FORMULA) || true

reinstall: uninstall install

start:
	brew services $@ $(FORMULA)

service: start

stop:
	brew services $@ $(FORMULA)

restart:
	brew services $@ $(FORMULA)

info:
	brew services $@ $(FORMULA)

status: info

log:
	@echo "Tailing log: $(LOG_FILE)"
	tail -f $(LOG_FILE)

tail: log

test:
	brew test ./Formula/$(FORMULA).rb

audit:
	brew audit --strict --online ./Formula/$(FORMULA).rb

lint:
	brew style ./Formula/$(FORMULA).rb

.PHONY: help install uninstall reinstall service stop restart log test audit lint
