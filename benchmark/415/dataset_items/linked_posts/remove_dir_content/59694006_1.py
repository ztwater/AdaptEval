import os
import glob

folders = glob.glob('./path/to/parentdir/*')
for fo in folders:
  file = glob.glob(f'{fo}/*')
  for f in file:
    os.remove(f)
