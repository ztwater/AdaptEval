def bfs_walk(directories):
    listdirs = [os.listdir(d) for d in directories]
    files    = [[fn for fn in listdir if os.path.isfile(os.path.join(dir,fn))] for listdir, dir in zip(listdirs, directories)]
    dirs     = [[dn for dn in listdir if os.path.isdir(os.path.join(dir,dn))]  for listdir, dir in zip(listdirs, directories)]

    for dirname, dirnames, filenames in zip(directories, dirs, files):
        yield dirname, dirnames, filenames

    directories = sum([list(map(lambda child: os.path.join(parent, child), children)) for parent, children in zip(directories, dirs)], [])
    for dirname, dirnames, filenames in bfs_walk(directories):
        yield dirname, dirnames, filenames
