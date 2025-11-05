import urllib2
import socket

class MyException(Exception):
    pass

try:
    urllib2.urlopen("http://example.com", timeout = 1)
except urllib2.URLError, e:
    # For Python 2.6
    if isinstance(e.reason, socket.timeout):
        raise MyException("There was an error: %r" % e)
    else:
        # reraise the original error
        raise
except socket.timeout, e:
    # For Python 2.7
    raise MyException("There was an error: %r" % e)
