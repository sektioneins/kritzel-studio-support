#!/usr/bin/env bash
# Crop + convert screenshots to WebP for the manual. Usage: process.sh <shots_dir> <out_root>
set -euo pipefail
src="$1"; out="$2"
declare -A crop=(
  [color_picker]=720x1360+790+20
  [preset_editor]=760x1020+770+200
  [text_dialog]=780x930+760+245
  [new_project]=850x900+730+260
  [about]=830x730+740+340
  [export]=850x900+730+260
  [export_svg]=850x700+730+355
  [export_pdf]=850x700+730+355
  [preset_picker]=1000x620+0+820
  [settings_1]=860x1440+730+0
  [settings_2]=860x1440+730+0
  [settings_3]=860x1440+730+0
  [settings_4]=860x1440+730+0
  [settings_advanced]=860x1440+730+0
)
for lang in en de; do
  mkdir -p "$out/$lang/img"
  for f in "$src/${lang}"_*.png; do
    name="$(basename "$f" .png)"; name="${name#${lang}_}"
    [[ "$name" == project_info ]] && continue
    args=()
    if [[ -n "${crop[$name]:-}" ]]; then args+=(-crop "${crop[$name]}" +repage); fi
    magick "$f" "${args[@]}" -resize '1600x1600>' -quality 82 -define webp:method=6 "$out/$lang/img/$name.webp"
  done
done
