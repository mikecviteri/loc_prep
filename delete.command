#!/usr/local/bin/python3

import shutil
import os

# Files to be deleted
lst = ['Audio files_prep', 'Audio_files_01', 'Audio_files_02', 'Beep_01', 'Beep_02', 'markers.mid', 'markers.tsv']
path = os.path.expanduser("~/Documents/Session prep/")


# Function to delete all files
def delete():
    for i in lst:
        try:
            shutil.rmtree(os.path.join(path, i))
        except NotADirectoryError:
            os.remove(os.path.join(path, i))
        except FileNotFoundError:
            pass
    return None


if __name__ == '__main__':
    delete()
