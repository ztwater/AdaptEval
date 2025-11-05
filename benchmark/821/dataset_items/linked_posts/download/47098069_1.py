import wget
import urllib
import time
from functools import wraps

def profile(func):
    @wraps(func)
    def inner(*args):
        print func.__name__, ": starting"
        start = time.time()
        ret = func(*args)
        end = time.time()
        print func.__name__, ": {:.2f}".format(end - start)
        return ret
    return inner

url1 = 'http://host.com/500a.iso'
url2 = 'http://host.com/500b.iso'
url3 = 'http://host.com/500c.iso'

def do_nothing(*args):
    pass

@profile
def urlretrive_test(url):
    return urllib.urlretrieve(url)

@profile
def wget_no_bar_test(url):
    return wget.download(url, out='/tmp/', bar=do_nothing)

@profile
def wget_with_bar_test(url):
    return wget.download(url, out='/tmp/')

urlretrive_test(url1)
print '=============='
time.sleep(1)

wget_no_bar_test(url2)
print '=============='
time.sleep(1)

wget_with_bar_test(url3)
print '=============='
time.sleep(1)
