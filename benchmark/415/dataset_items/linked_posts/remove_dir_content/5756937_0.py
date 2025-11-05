import os
import glob

files = glob.glob('/YOUR/PATH/*')
for f in files:
    os.remove(f)
