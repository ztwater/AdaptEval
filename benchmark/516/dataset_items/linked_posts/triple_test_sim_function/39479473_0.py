# Create a directory and any missing ancestor directories. 
# If the directory already exists, do nothing.

from distutils.dir_util import mkpath
mkpath("test")    
