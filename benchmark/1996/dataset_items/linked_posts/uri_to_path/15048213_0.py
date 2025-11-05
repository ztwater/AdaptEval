>>> from urllib.parse import unquote, urlparse
>>> unquote(urlparse('file:///home/user/some%20file.txt').path)
'/home/user/some file.txt'
