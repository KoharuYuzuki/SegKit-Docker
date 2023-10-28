# SegKit-Docker
[segmentation-kit](https://github.com/julius-speech/segmentation-kit) + Docker の音素セグメンテーション支援システムです  

## 準備
1. 音素セグメンテーションを行いたいWAVファイルを`wav`ディレクトリに配置します
1. WAVファイルの音声を書き起こしたテキストファイルを`txt`ディレクトリに配置します

WAVファイルのサンプリングレート及びコーデックは任意のものを使用できます  
テキストファイルは１行で記述し、UTF-8形式でひらがな及び読点のみ使用できます  
準備が完了すると次のようなファイル配置になります  

```
ファイル配置例

SegKit
├─ wavex
│  ├─ 001.wav
│  ├─ 002.wav
│  └─ 003.wav
├─ txt
│  ├─ 001.txt
│  ├─ 002.txt
│  └─ 003.txt
.
.
.
```

### Tips
ITAコーパスのセグメンテーションを行う場合は、[ITA-Hiragana](https://github.com/KoharuYuzuki/ITA-Hiragana) にひらがなに変換済みの書き起こしファイルがあります  

## セグメンテーション
以下のコマンドを実行します  

```
# Dockerコンテナ起動
$ docker-compose build --no-cache
$ docker-compose up -d

# セグメンテーション
$ docker-compose run app bash
$ /workspace/run.sh
$ exit

# Docckerコンテナ停止
$ docker-compose down
```

### Tips
0バイトのラベルが生成される場合、セグメンテーションに失敗しています  
詳細は`log`ディレクトリを確認してください  

## ライセンス
Copyright (c) 2023 KoharuYuzuki  
MIT License (https://opensource.org/license/mit/)  
