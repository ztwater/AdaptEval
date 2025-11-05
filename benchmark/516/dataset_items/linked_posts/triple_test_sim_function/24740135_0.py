try:
    os.makedirs(path)
except OSError as exception:
    if exception.errno != errno.EEXIST:
        raise
    else:
        print "\nBE CAREFUL! Directory %s already exists." % path
