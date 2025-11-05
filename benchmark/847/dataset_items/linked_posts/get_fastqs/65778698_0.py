import os, re, glob

path = '/home/my/path'
files = glob.glob(os.path.join(path, '*.png'))
files.sort(key=lambda x:[int(c) if c.isdigit() else c for c in re.split(r'(\d+)', x)])
for infile in files:
    print(infile)
