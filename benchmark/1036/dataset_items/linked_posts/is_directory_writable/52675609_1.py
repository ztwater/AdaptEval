$ python dir-test.py -h
usage: dir-test.py [-h] [-d DIR]

optional arguments:
  -h, --help         show this help message and exit
  -d DIR, --dir DIR  Directory to use. Default: /tmp

$ python dir-test.py -d /not/real
usage: dir-test.py [-h] [-d DIR]
dir-test.py: error: argument -d/--dir: /not/real is not writable or does not exist.

$ python dir-test.py -d ~
