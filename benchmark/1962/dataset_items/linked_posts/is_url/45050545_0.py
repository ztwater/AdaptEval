from urlparse import urlparse
def url_check(url):

    min_attr = ('scheme' , 'netloc')
    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]):
            return True
        else:
            return False
    except:
        return False
