import errno
try:
    os.makedirs(d)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
