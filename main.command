#!/usr/local/bin/python3

import pandas as pd
from audio import get_duration, create_audios
import os
import shutil

# Retrieve files from folder
f_path = os.path.expanduser("~/Documents/Session prep/")
os.mkdir(f_path) if not os.path.exists(f_path) else None
audios = f_path + 'Audio files'
beep = f_path + 'Beep.wav'
beep_duration = get_duration(beep)
result_dir = f_path + 'Audio files_prep'

# Read csv files
csv_file = f_path + 'Tracker_filtered.csv'
table = pd.read_csv(csv_file, low_memory=False)

# Create beep and files folders
dirs = ['Beep', 'Audio_files']
save_paths = []
characters = {}
char_lines = {}

for i in range(1, 3):
    for j in dirs:
        path = os.path.join(f_path, '{}_0{}'.format(j, i))
        save_paths.append(path)
        os.mkdir(path) if not os.path.exists(path) else None

os.mkdir(result_dir) if not os.path.exists(result_dir) else None


# Converting sss to mmm:ss.sss
def convert_ms(ms):
    seconds = int((ms / 1000) % 60)
    minutes = int((ms / (1000 * 60)) % 60)
    mms = int(ms - ((minutes * 60000) + (seconds * 1000)))
    return '{:03d}:{:02d}.{:03d}'.format(minutes, seconds, mms)


# Creating tsv file for Pro Tools markers
def markers(chars):
    mm_ss_ms = list(map(lambda x: convert_ms(x), chars.values()))

    for idx, char in enumerate(chars):
        chars[char] = mm_ss_ms[idx]

    with open(f'{f_path}markers.tsv', 'w') as f:
        for line, location in chars.items():
            print('{}\t{}'.format(line, location), file=f)


# Running script
def run(time_code=0):
    count = 1
    for elem in range(table.shape[0]):
        character = table.loc[elem, "Character"]
        characters.update({character: time_code}) if character not in characters.keys() else None
        audio_file = os.path.join(audios, f'{str(table.loc[elem, "SIDE ID"])}.wav')
        duration = get_duration(audio_file)
        time_code += (duration + beep_duration) * 2

        for n in range(0, 4):
            create_audios(table.loc[elem, 'SIDE ID'], duration,
                          beep if n % 2 == 0 else audio_file, save_paths, n, count)
            count += 1
    return characters


def move_folders():
    for folder in save_paths:
        shutil.move(folder, result_dir)
    return None


def info():
    counter = '\n{:^64s}\n{:^64s}\n{:^64s}\n'.format('*' * 24, str(len(table.index)) + ' total audiofiles/rows',
                                                     '*' * 24)
    print(counter)

    unique_chars = table['Character'].value_counts().index.tolist()

    for idx, value in enumerate(table['Character'].value_counts()):
        print('{:^64s}'.format('* ' + unique_chars[idx] + ' --- ' + str(value) + ' lines\n'))
    
    print(f'\nSaved to: {result_dir}\n\n')

if __name__ == '__main__':
    all_chars = run()
    markers(all_chars)
    move_folders()
    info()
