try:
    urllib2.urlopen("http://example.com", timeout = 1)
except urllib2.URLError, e:
    raise MyException("There was an error: %r" % e)
