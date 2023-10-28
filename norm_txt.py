import glob
import os

txt_file_paths = sorted(glob.glob('./txt/*.txt'))

for txt_file_path in txt_file_paths:
  with open(txt_file_path, mode='r', encoding='utf-8') as txt_file:
    text = txt_file.read()

  text = text.replace('、', ' sp ')
  text = text.replace('ゔ', 'ぶ')
  text = text.replace('てゃ', 'ちゃ')
  text = text.replace('てゅ', 'ちゅ')
  text = text.replace('てょ', 'ちょ')
  text = text.replace('んー', 'ん')

  txt_file_name = os.path.basename(txt_file_path)
  normalized_txt_file_path = os.path.join('/data', txt_file_name)

  with open(normalized_txt_file_path, mode='w', encoding='utf-8') as normalized_txt_file:
    normalized_txt_file.write(text)
