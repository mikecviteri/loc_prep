import wave
import contextlib
from pydub import AudioSegment
import os
import shutil


# Getting audio file duration
def get_duration(f_name):
    with contextlib.closing(wave.open(f_name, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration * 1000


beep = os.path.expanduser("~/Documents/Session prep/Beep.wav")
beep_duration = get_duration(beep)


# Creating an empty audio wav file
def make_file(name, dur, path):
    file = AudioSegment.silent(duration=dur, frame_rate=44100)
    file.export(os.path.join(path, name), format="wav")


# Copying/creating the timeline for each file (4 folders)
def create_audios(f_id, dur, file, folders, stop, number):
    for k in range(0, 4):
        if k != stop:
            make_file('{}_{}_{}.wav'.format(str(k + 1).zfill(2), str(number).zfill(2), f_id),
                      beep_duration if file == beep else dur, folders[k])
        else:
            shutil.copy(file, os.path.join(folders[k], '{}_{}_{}.wav'.
                                           format(str(k + 1).zfill(2), str(number).zfill(2), str(f_id))))
