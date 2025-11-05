>>> import re
>>> ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
>>> sometext = 'ls\r\n\x1b[00m\x1b[01;31mexamplefile.zip\x1b[00m\r\n\x1b[01;31m'
>>> ansi_escape.sub('', sometext)
'ls\r\nexamplefile.zip\r\n'
