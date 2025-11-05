from shutil import make_archive
make_archive(
  'zipfile_name', 
  'zip',           # the archive format - or tar, bztar, gztar 
  root_dir=None,   # root for archive - current working dir if None
  base_dir=None)   # start archiving from here - cwd if None too
