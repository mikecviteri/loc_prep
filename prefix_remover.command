#!/usr/local/bin/python3

import os
import re

pattern = re.compile(r'[\d]._.*_')


def rename(session_path):
    for i in os.listdir(session_path):
        new_name = 'Beep.wav' if i.startswith('01_b1_01_') else re.sub(pattern, "", i)
        os.rename('{}/{}'.format(session_path, i), '{}/{}'.format(session_path, new_name))


rename_path = input('Copy full path of audio files to rename')

if __name__ == '__main__':
    rename(rename_path)
