import pycurl

FILE_DEST = 'pycurl.html'
FILE_SRC = 'http://pycurl.io/'

with open(FILE_DEST, 'wb') as f:
    c = pycurl.Curl()
    c.setopt(c.URL, FILE_SRC)
    c.setopt(c.WRITEDATA, f)
    c.perform()
    c.close()
