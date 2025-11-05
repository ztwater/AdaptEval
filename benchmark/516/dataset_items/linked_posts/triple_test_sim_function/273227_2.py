import os, errno

try:
    os.makedirs(directory)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
