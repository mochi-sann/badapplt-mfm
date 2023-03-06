#!/bin/bash

# 画像が保存されているディレクトリのパス
IMAGES_DIR="./files/img/"

# 画像ファイルの拡張子
IMAGE_EXT="png"

OUTPUT_DIR="./files/new/"




# 出力フォルダが存在しない場合、作成する
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir "$OUTPUT_DIR"
fi

# 画像を半分にする
mogrify -path "$OUTPUT_DIR" -resize 5% "$IMAGES_DIR/*.$IMAGE_EXT"
