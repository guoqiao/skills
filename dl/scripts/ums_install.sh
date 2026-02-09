#!/bin/bash

set -ueo pipefail

conf_dir="$HOME/Library/Application Support/UMS"
conf_file="$conf_dir/UMS.conf"
[ -f "$conf_file" ] && exit 0

brew install --cask universal-media-server || true

mkdir -p "$conf_dir"
cat > "$conf_file" <<EOF
server_name = Claw Media Center
folders = ${HOME}/Movies,${HOME}/Music
hostname = 0.0.0.0
network_interface =
port = 5001
upnp_enabled = true
advertise_upnp = true
thumbnails = true
folder_monitor_enabled = true
authentication_enabled = false
EOF

echo "conf file path: $conf_file"
echo
cat "$conf_file"
echo
echo "You can access the web interface at: http://localhost:5001"
