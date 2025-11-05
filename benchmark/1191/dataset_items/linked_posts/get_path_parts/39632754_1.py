>>> for path in [
...         r'd:\stuff\morestuff\furtherdown\THEFILE.txt',
...         '/path/to/file.txt',
...         'relative/path/to/file.txt',
...         r'C:\path\to\file.txt',
...         r'\\host\share\path\to\file.txt',
...     ]:
...     print parts(path), os.path.join(*parts(path))
... 
['d:\\', 'stuff', 'morestuff', 'furtherdown', 'THEFILE.txt'] d:\stuff\morestuff\furtherdown\THEFILE.txt
['/', 'path', 'to', 'file.txt'] /path\to\file.txt
['', 'relative', 'path', 'to', 'file.txt'] relative\path\to\file.txt
['C:\\', 'path', 'to', 'file.txt'] C:\path\to\file.txt
['\\\\', 'host', 'share', 'path', 'to', 'file.txt'] \\host\share\path\to\file.txt
