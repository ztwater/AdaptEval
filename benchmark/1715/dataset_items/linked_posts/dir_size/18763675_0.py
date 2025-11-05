def getFolderSize(p):
   from functools import partial
   prepend = partial(os.path.join, p)
   return sum([(os.path.getsize(f) if os.path.isfile(f) else getFolderSize(f)) for f in map(prepend, os.listdir(p))])
