import os
import glob
print(sum(os.path.getsize(f) for f in glob.glob('**', recursive=True) if os.path.isfile(f))/(1024*1024))
