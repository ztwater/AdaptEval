import fnmatch

print len(fnmatch.filter(os.listdir(dirpath), '*.txt'))
