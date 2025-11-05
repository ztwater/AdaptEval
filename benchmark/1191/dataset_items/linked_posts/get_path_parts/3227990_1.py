>>> for i in open("filedata.txt").readlines():
...     print i.strip().split("\\")
... 
['d:', 'stuff', 'morestuff', 'furtherdown', 'THEFILE.txt']
['d:', 'otherstuff', 'something', 'otherfile.txt']
