>>> from os.path import exists
>>> from sys import platform
>>> drives = ''.join( l for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' if exists('%s:/'%l) ) if platform=='win32' else ''
>>> drives
'CZ'
