import urllib2
import socket

class MyException(Exception):
    pass

try:
    urllib2.urlopen("http://example.com", timeout = 1)
except urllib2.URLError as e:
    print type(e)    #not catch
except socket.timeout as e:
    print type(e)    #catched
    raise MyException("There was an error: %r" % e)
