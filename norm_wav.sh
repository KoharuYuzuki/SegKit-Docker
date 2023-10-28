set -eu

cd ./wav
for file in *.wav; do ffmpeg -i "$file" -ar 16000 -acodec pcm_s16le "/data/$file"; done
