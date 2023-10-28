set -eu

CURRENT_DIR=$(cd $(dirname $0); pwd)

cd "$CURRENT_DIR"
mkdir -p wav
mkdir -p txt
mkdir -p log
mkdir -p julius_lab
mkdir -p openjtalk_lab
./norm_wav.sh
python3 norm_txt.py

./segmentation.sh

cd /data
for file in *.lab; do cp "$file" "/workspace/julius_lab/$file"; done
for file in *.log; do cp "$file" "/workspace/log/$file"; done

cd "$CURRENT_DIR"
python3 julius2openjtalk.py
