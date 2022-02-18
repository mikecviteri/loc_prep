import pandas as pd
from audio import get_duration, create_audios
import os


def run():
    # Retrieve files from folder
    fpath = os.path.expanduser("~/Documents/Session prep/")
    os.mkdir(fpath) if not os.path.exists(fpath) else None
    audios = fpath + 'Audio files'
    beep = fpath + 'Beep.wav'

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

    # Running script
    count = 1
    for i in table['SIDE ID']:
        audio_file = os.path.join(audios, f'{str(i)}.wav')
        duration = get_duration(audio_file)

        for n in range(0, 4):
            create_audios(i, duration, beep if n % 2 == 0 else audio_file, save_paths, n, count)
            count += 1
    return None


if __name__ == '__main__':
    run()
