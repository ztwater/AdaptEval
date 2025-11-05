import os
import glob

files = glob.glob(r'path/*')
for items in files:
    os.remove(items)
