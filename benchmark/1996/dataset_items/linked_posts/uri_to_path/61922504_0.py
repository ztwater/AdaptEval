try:
    from urllib.parse import urlparse, unquote
    from urllib.request import url2pathname
except ImportError:
    # backwards compatability
    from urlparse import urlparse
    from urllib import unquote, url2pathname


def uri_to_path(uri):
    parsed = urlparse(uri)
    host = "{0}{0}{mnt}{0}".format(os.path.sep, mnt=parsed.netloc)
    return os.path.normpath(
        os.path.join(host, url2pathname(unquote(parsed.path)))
    )
