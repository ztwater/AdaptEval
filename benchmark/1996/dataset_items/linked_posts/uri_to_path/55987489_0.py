import urllib.parse
url_data = urllib.parse.urlparse('file:///home/user/some%20file.txt')
path = urllib.parse.unquote(url_data.path)
