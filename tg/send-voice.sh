#!/bin/bash

set -ueo pipefail

filepath=${1:-voice.ogg}

curl -sS -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendVoice \
    -F disable_notification=true \
    -F chat_id=${TELEGRAM_CHAT_ID} \
    -F voice=@${filepath} | jq
