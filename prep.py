import pandas as pd
from audio import get_duration
import os

# Create folders
#
# folders = ['Beep', 'Audiofiles']
#
# for i in range(1, 3):
#     for j in folders:
#         path = os.path.join(os.getcwd(), '{}_0{}'.format(j, i))
#         os.mkdir(path)

csv_file = '/Users/miguelcampero/Desktop/Desktop Files/Scripts/NH/NH_scene_script/Pruebas.csv'
table = pd.read_csv(csv_file, low_memory=False)

audios = '/Users/miguelcampero/Desktop/Untitled/Audio Files'

beep = '/Users/miguelcampero/Desktop/Untitled/Audio Files/Beep.wav'

file = 1

for i in table['SIDE ID']:
    x = os.path.join(audios, f'{str(i)}.wav')
    print(i, get_duration(x))

