import os
from pathlib import Path   # This demo requires pip install for Python < 3.4
import sys
try:
    from urllib.parse import urlparse, unquote
    from urllib.request import url2pathname
except ImportError:  # backwards compatability:
    from urlparse import urlparse
    from urllib import unquote, url2pathname

DIVIDER = "-" * 30

if sys.platform == "win32":  # WINDOWS
    filepaths = [
        r"C:\Python27\Scripts\pip.exe",
        r"C:\yikes\paths with spaces.txt",
        r"\\localhost\c$\WINDOWS\clock.avi",
        r"\\networkstorage\homes\rdekleer",
    ]
else:  # *NIX
    filepaths = [
        os.path.expanduser("~/.profile"),
        "/usr/share/python3/py3versions.py",
    ]

for path in filepaths:
    uri = Path(path).as_uri()
    parsed = urlparse(uri)
    host = "{0}{0}{mnt}{0}".format(os.path.sep, mnt=parsed.netloc)
    normpath = os.path.normpath(
        os.path.join(host, url2pathname(unquote(parsed.path)))
    )
    absolutized = os.path.abspath(
        os.path.join(host, url2pathname(unquote(parsed.path)))
    )
    result = ("{DIVIDER}"
              "\norig path:       \t{path}"
              "\nconverted to URI:\t{uri}"
              "\nrebuilt normpath:\t{normpath}"
              "\nrebuilt abspath:\t{absolutized}").format(**locals())
    print(result)
    assert path == absolutized
