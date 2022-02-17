import wave
import contextlib
from pydub import AudioSegment
import os


def get_duration(fname):
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration * 1000


def make_file(name, dur, path):
    file = AudioSegment.silent(duration=dur)
    file.export(os.path.join(path, name), format="wav")

