import pandas as pd
from audio import get_duration, make_file
import os
import shutil

# Create folders

folders = ['Beep', 'Audiofiles']
save_paths = []

for i in range(1, 3):
    for j in folders:
        path = os.path.join(os.getcwd(), '{}_0{}'.format(j, i))
        save_paths.append(path)
        os.mkdir(path) if not os.path.exists(path) else None

# CSV
csv_file = '/Users/miguelcampero/Desktop/Desktop Files/Scripts/NH/NH_scene_script/Pruebas.csv'

table = pd.read_csv(csv_file, low_memory=False)

# FOLDERS
audios = '/Users/miguelcampero/Desktop/Untitled/Audio Files'
beep = '/Users/miguelcampero/Desktop/Untitled/Audio Files/Beep.wav'
beep_duration = get_duration(beep)

count = 1





# SCRIPT
for i in table['SIDE ID']:
    file = os.path.join(audios, f'{str(i)}.wav')
    duration = get_duration(file)

    # 1
    shutil.copy(beep, os.path.join(save_paths[0], '01_{}_{}.wav'.format(str(count).zfill(2), str(i))))
    for j in range(1, 4):
        make_file('{}_{}_{}.wav'.format(str(j + 1).zfill(2), str(count).zfill(2), i), beep_duration, save_paths[j])
    count += 1

    # 2
    shutil.copy(file, os.path.join(save_paths[0], '01_{}_{}.wav'.format(str(count).zfill(2), str(i))))
    for j in range(1, 4):
        make_file('{}_{}_{}.wav'.format(str(j + 1).zfill(2), str(count).zfill(2), i), duration, save_paths[j])
    count += 1


    # #3
    # print(save_paths[2])
    #
    # # #4
    # print(save_paths[3])

    #
    #
    #
    # #audiofile
    # shutil.copy(file, os.path.join(os.getcwd(), str(count) + str(i)+'.wav'))
    #
    # #Silent audiofile
    # make_file(duration)



    # BEEP 1
    # BEEP   >  SILENCIO AUDIO   >  SILENCIO BEEP  > SILENCIO AUDIO

    # AUDIOFILES 1
    # 2. SILENCIO BEEP  >  	     AUDIO		      >  SILENCIO BEEP  > SILENCIO AUDIO

    # BEEP 2
    # 3. SILENCIO BEEP  >   SILENCIO AUDIO   >           BEEP         > SILENCIO AUDIO

    # AUDIOFILES 2
    # 4. SILENCIO BEEP  >   SILENCIO AUDIO   > SILENCIO BEEP  >  AUDIO
