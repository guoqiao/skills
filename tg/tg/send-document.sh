#!/bin/bash

set -ueo pipefail

filepath=${1:-document.pdf}

source ~/opt/telegram/.env

curl -sS -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendDocument \
    -F disable_notification=true \
    -F chat_id=${TELEGRAM_CHAT_ID} \
    -F document=@${filepath} | jq
