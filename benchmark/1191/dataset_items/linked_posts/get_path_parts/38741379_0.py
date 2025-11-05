>>> from pathlib import Path
>>> Path('C:/path/to/file.txt').parts
('C:\\', 'path', 'to', 'file.txt')
>>> Path(r'C:\path\to\file.txt').parts
('C:\\', 'path', 'to', 'file.txt')
