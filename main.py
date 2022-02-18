import pandas as pd
from audio import get_duration, create_audios
import os

# Retrieve files from folder
fpath = os.path.expanduser("~/Documents/Session prep/")
os.mkdir(fpath) if not os.path.exists(fpath) else None
audios = fpath + 'Audio files'
beep = fpath + 'Beep.wav'
beep_duration = get_duration(beep)

# Read csv files
csv_file = fpath + 'Tracker_filtered.csv'
table = pd.read_csv(csv_file, low_memory=False)

# Create beep and files folders
dirs = ['Beep', 'Audiofiles']
save_paths = []

for i in range(1, 3):
    for j in dirs:
        path = os.path.join(fpath, '{}_0{}'.format(j, i))
        save_paths.append(path)
        os.mkdir(path) if not os.path.exists(path) else None

characters = {}


# Running script
def run(timecode=0):
    count = 1
    for elem in range(table.shape[0]):
        character = table.loc[elem, "Character"]
        characters.update({character: timecode}) if character not in characters.keys() else None
        audio_file = os.path.join(audios, f'{str(table.loc[elem, "SIDE ID"])}.wav')
        duration = get_duration(audio_file)
        timecode += (duration + beep_duration) * 2

        for n in range(0, 4):
            create_audios(table.loc[elem, 'SIDE ID'], duration,
                          beep if n % 2 == 0 else audio_file, save_paths, n, count)
            count += 1
    return characters


def convert_ms(ms):
    seconds = int((ms / 1000) % 60)
    minutes = int((ms / (1000 * 60)) % 60)
    mms = int(ms - ((minutes * 60000) + (seconds * 1000)))
    return '{:03d}:{:02d}.{:03d}'.format(minutes, seconds, mms)


def markers(chars):
    mm_ss_ms = list(map(lambda x: convert_ms(x), chars.values()))

    for idx, char in enumerate(chars):
        chars[char] = mm_ss_ms[idx]

    with open(f'{fpath}markers.tsv', 'w') as f:
        for line, location in chars.items():
            print('{}\t{}'.format(line, location), file=f)


if __name__ == '__main__':
    all_chars = run()
    markers(all_chars)
