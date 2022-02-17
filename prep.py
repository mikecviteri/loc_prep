import pandas as pd
from audio import get_duration, create_audios
import os

# Folders
audios = '/Users/miguelcampero/Desktop/Untitled/Audio Files'
beep = '/Users/miguelcampero/Desktop/Untitled/Audio Files/Beep.wav'

# csv
csv_file = '/Users/miguelcampero/Desktop/Desktop Files/Scripts/NH/NH_scene_script/Pruebas.csv'
table = pd.read_csv(csv_file, low_memory=False)

# Create folders
dirs = ['Beep', 'Audiofiles']
save_paths = []

for i in range(1, 3):
    for j in dirs:
        path = os.path.join(os.getcwd(), '{}_0{}'.format(j, i))
        save_paths.append(path)
        os.mkdir(path) if not os.path.exists(path) else None

# Script
count = 1
for i in table['SIDE ID']:
    audio_file = os.path.join(audios, f'{str(i)}.wav')
    duration = get_duration(audio_file)

    for n in range(0, 4):
        create_audios(i, duration, beep if n % 2 == 0 else audio_file, save_paths, n, count)
        count += 1
