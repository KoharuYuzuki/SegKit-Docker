import glob
import re
import os

julius_lab_file_paths = sorted(glob.glob('./julius_lab/*.lab'))
lab_pattern = re.compile('^(?P<begin>[0-9.]+) (?P<end>[0-9.]+) (?P<phoneme>[a-z]+)$', re.M | re.I)

for julius_lab_file_path in julius_lab_file_paths:
  with open(julius_lab_file_path, mode='r', encoding='utf-8') as julius_lab_file:
    julius_label = julius_lab_file.read()

  matches = [x.groupdict() for x in re.finditer(lab_pattern, julius_label)]

  lab_file_name = os.path.basename(julius_lab_file_path)
  openjtalk_lab_file_path = os.path.join('./openjtalk_lab', lab_file_name)

  with open(openjtalk_lab_file_path, mode='w', encoding='utf-8') as openjtalk_lab_file:
    for match in matches:
      begin   = int(float(match['begin']) * 1e+7)
      end     = int(float(match['end']) * 1e+7)
      phoneme = match['phoneme']

      if phoneme == 'silB':
        phoneme = 'sil'
      elif phoneme == 'silE':
        phoneme = 'sil'
      elif phoneme == 'q':
        phoneme = 'cl'
      elif phoneme == 'sp':
        phoneme = 'pau'

      openjtalk_lab_file.write(F'{begin} {end} {phoneme}\n')
