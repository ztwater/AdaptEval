from urllib.request import urlretrieve

url = 'http://mirror.pnl.gov/releases/16.04.2/ubuntu-16.04.2-desktop-amd64.iso'
dst = 'ubuntu-16.04.2-desktop-amd64.iso'
urlretrieve(url, dst)
