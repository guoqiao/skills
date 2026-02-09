#!/bin/bash

# Universal Media Server Uninstall Script

set -e

killall UMS >/dev/null 2>&1 || true
brew uninstall --cask universal-media-server >/dev/null 2>&1 || true
rm -rf "$HOME/Library/Application Support/UMS"
rm -rf "$HOME/Library/Caches/Homebrew/Cask/UMS-"*
rm -rf "$HOME/Library/Preferences/com.universalmediaserver."*
rm -rf "/Applications/Universal Media Server.app"