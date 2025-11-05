import os
sorted(glob.glob('*.png'), key=os.path.getsize)
