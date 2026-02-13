#!/bin/bash

set -ueo pipefail

text=${1:-"Hello!"}

curl -sS -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
    -d chat_id=${TELEGRAM_CHAT_ID} \
    -d text="${text}" | jq
