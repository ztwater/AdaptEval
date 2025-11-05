import os
DIR = os.list('Folder')
for i in range(len(DIR)):
    os.remove('Folder'+chr(92)+i)
