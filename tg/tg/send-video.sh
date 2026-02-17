#!/bin/bash

set -ueo pipefail

filepath=${1:-video.mp4}

curl -sS -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendVideo \
    -F disable_notification=true \
    -F chat_id=${TELEGRAM_CHAT_ID} \
    -F video=@${filepath} | jq
