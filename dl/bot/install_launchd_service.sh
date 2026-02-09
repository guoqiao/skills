#!/bin/bash

set -ueo pipefail

LABEL="me.guoqiao.dlbot"
PLIST_PATH="$HOME/Library/LaunchAgents/${LABEL}.plist"
LOG_PATH="$HOME/Library/Logs/${LABEL}.log"
BOT_DIR="$(cd "$(dirname "$0")" && pwd)"
UV="$(command -v uv)"

cat > "$PLIST_PATH" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${LABEL}</string>

    <key>ProgramArguments</key>
    <array>
        <string>${UV}</string>
        <string>run</string>
        <string>--env-file</string>
        <string>.env</string>
        <string>bot.py</string>
    </array>

    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>${PATH}</string>
    </dict>

    <key>WorkingDirectory</key>
    <string>${BOT_DIR}</string>

    <key>RunAtLoad</key>
    <true/>

    <key>KeepAlive</key>
    <true/>

    <key>StandardOutPath</key>
    <string>${LOG_PATH}</string>

    <key>StandardErrorPath</key>
    <string>${LOG_PATH}</string>
</dict>
</plist>
EOF

echo "Plist written to: $PLIST_PATH"

# Unload if already loaded, ignore errors.
launchctl bootout --wait "gui/$(id -u)/${LABEL}" 2>/dev/null || true

launchctl bootstrap "gui/$(id -u)" "$PLIST_PATH"
echo "Service loaded: $LABEL"
echo "Log: $LOG_PATH"
