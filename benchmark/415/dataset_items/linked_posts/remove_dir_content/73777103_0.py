import os
import glob

def truncate(path):
    files = glob.glob(path+'/*.*')
    for f in files:
        os.remove(f)

truncate('/my/path')
