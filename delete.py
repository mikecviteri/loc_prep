import shutil
import os

lst = ['Audiofiles_01', 'Audiofiles_02', 'Beep_01', 'Beep_02', 'markers.mid', 'markers.tsv']
path = os.path.expanduser("~/Documents/Session prep/")


def delete():
    for i in lst:
        try:
            shutil.rmtree(os.path.join(path, i))
        except FileNotFoundError:
            os.remove(os.path.join(path, i))
    return None


if __name__ == '__main__':
    delete()
