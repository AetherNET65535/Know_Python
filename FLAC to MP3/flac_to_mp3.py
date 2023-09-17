import os
from pydub import AudioSegment

# input and output folder path
input_folder = 'FLAC MUSIC'
output_folder = 'MP3 MUSIC'

# create output folder (if not exist lah)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# see see all Flac file in the folder
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.flac'):
            flac_file_path = os.path.join(root, file)
            mp3_file_path = os.path.join(output_folder, file.replace('.flac', '.mp3'))

            # use pydub load Flac file
            audio = AudioSegment.from_file(flac_file_path, format='flac')

            # convert to mp3 and put to a pro pro folder~
            audio.export(mp3_file_path, format='mp3')

# SEE BRO KEDO STEAM OR NOT!!
if any(file.endswith('.flac') for _, _, files in os.walk(input_folder) for file in files):
    print(f'Bro have {len([file for _, _, files in os.walk(input_folder) for file in files if file.endswith(".flac")])} FAKE FAKE Done YAA!!')
else:
    print('Bro is Real Real DONE YAAA!!')