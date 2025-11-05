>>> from pathlib import PurePosixPath, PureWindowsPath
>>> PurePosixPath('/path/to/file.txt').parts
('/', 'path', 'to', 'file.txt')
>>> PureWindowsPath(r'C:\path\to\file.txt').parts
('C:\\', 'path', 'to', 'file.txt')
>>> PureWindowsPath(r'\\host\share\path\to\file.txt').parts
('\\\\host\\share\\', 'path', 'to', 'file.txt')
