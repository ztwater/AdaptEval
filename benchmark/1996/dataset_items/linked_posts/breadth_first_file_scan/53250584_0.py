def rbf_walk(path):
    dirlist = ((dirpath.count(os.path.sep), dirpath, dirnames, filenames) for
        dirpath, dirnames, filenames in os.walk(path, topdown = False))
    for entry in sorted(dirlist, reverse = True):
        yield entry[1:]
