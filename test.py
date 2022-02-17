import shutil
import os

lst = ['Audiofiles_01', 'Audiofiles_02', 'Beep_01', 'Beep_02']

for i in lst:
    path = os.path.join(os.getcwd(), i)
    shutil.rmtree(path)
