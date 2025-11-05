import os
import errno

gdsfile  = "/home/hha/temp.gds"
try:
    os.close(os.open(gdsfile, os.O_CREAT|os.O_EXCL))
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
