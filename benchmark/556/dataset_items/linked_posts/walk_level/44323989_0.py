baselevel = len(rootdir.split(os.path.sep))
for subdirs, dirs, files in os.walk(rootdir):
    curlevel = len(subdirs.split(os.path.sep))
    if curlevel <= baselevel + 1:
        [do stuff]
