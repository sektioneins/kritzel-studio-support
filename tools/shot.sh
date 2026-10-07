#!/usr/bin/env bash
# Usage: shot.sh <name>  — capture device screen to shots/<name>.png and a 50% preview
set -euo pipefail
sleep "${2:-1.5}"
dir="$(dirname "$0")/shots"
adb exec-out screencap -p > "$dir/$1.png"
magick "$dir/$1.png" -resize 50% "$dir/_preview.png"
