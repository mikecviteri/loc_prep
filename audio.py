import wave
import contextlib
from pydub import AudioSegment
import os
import shutil


def get_duration(fname):
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration * 1000


def make_file(name, dur, path):
    file = AudioSegment.silent(duration=dur, frame_rate=44100)
    file.export(os.path.join(path, name), format="wav")


beep = os.path.expanduser("~/Documents/Session prep/Beep.wav")
beep_duration = get_duration(beep)


def create_audios(f_id, dur, file, folders, stop, number):
    for k in range(0, 4):
        if k != stop:
            make_file('{}_{}_{}.wav'.format(str(k + 1).zfill(2), str(number).zfill(2), f_id),
                      beep_duration if file == beep else dur, folders[k])
        else:
            shutil.copy(file, os.path.join(folders[k], '{}_{}_{}.wav'.
                                           format(str(k + 1).zfill(2), str(number).zfill(2), str(f_id))))
