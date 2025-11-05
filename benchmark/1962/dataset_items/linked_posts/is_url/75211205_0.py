from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

url = 'http://google.com'
if is_valid_url(url):
    print('Valid URL')
else:
    print('Malformed URL')
