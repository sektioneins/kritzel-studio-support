#!/usr/bin/env bash
# Usage: tap.sh x y  — coordinates in 50%-preview space (doubled for device)
set -euo pipefail
adb shell input tap $(( $1 * 2 )) $(( $2 * 2 ))
