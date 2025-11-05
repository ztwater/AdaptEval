def rm(f):
    if os.path.isdir(f): return os.rmdir(f)
    if os.path.isfile(f): return os.unlink(f)
    raise TypeError, 'must be either file or directory'

map( rm, (os.path.join( mydir,f) for f in os.listdir(mydir)) )
