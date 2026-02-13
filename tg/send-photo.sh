#!/bin/bash

set -ueo pipefail

filepath=${1:-image.png}

curl -sS -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendPhoto \
    -F disable_notification=true \
    -F chat_id=${TELEGRAM_CHAT_ID} \
    -F photo=@${filepath} | jq
