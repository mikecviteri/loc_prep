import wave
import contextlib
from pydub import AudioSegment


def get_duration(fname):
    with contextlib.closing(wave.open(fname, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return duration
#
# x = AudioSegment.silent(duration=1000)
