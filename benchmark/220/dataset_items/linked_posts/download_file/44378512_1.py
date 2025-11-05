from urllib.request import urlopen
from shutil import copyfileobj
from tempfile import NamedTemporaryFile

url = 'http://mirror.pnl.gov/releases/16.04.2/ubuntu-16.04.2-desktop-amd64.iso'
with urlopen(url) as fsrc, NamedTemporaryFile(delete=False) as fdst:
    copyfileobj(fsrc, fdst)
