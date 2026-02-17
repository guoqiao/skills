#!/bin/bash

set -ueo pipefail

filepath=${1:-audio.mp3}

curl -sS -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendAudio \
    -F disable_notification=true \
    -F chat_id=${TELEGRAM_CHAT_ID} \
    -F audio=@${filepath} | jq
