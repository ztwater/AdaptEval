import os
def parts(path):
    p,f = os.path.split(path)
    return parts(p) + [f] if f else [os.path.splitdrive(p)]

[('d:', '\\'), 'stuff', 'morestuff', 'furtherdown', 'THEFILE.txt']
[('', '/'), 'path', 'to', 'file.txt']
[('', ''), 'relative', 'path', 'to', 'file.txt']
[('C:', '\\'), 'path', 'to', 'file.txt']
[('', '\\\\'), 'host', 'share', 'path', 'to', 'file.txt']
