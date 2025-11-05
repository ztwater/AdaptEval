import os
dir = "/path/to/files/"

#List all files immediately under this folder:
print ( next( os.walk(dir) )[2] )

#List all folders immediately under this folder:
print ( next( os.walk(dir) )[1] )
