import urllib
from pprint import pprint

invalid_url = 'dkakasdkjdjakdjadjfalskdjfalk'
valid_url = 'https://stackoverflow.com'
tokens = [urllib.parse.urlparse(url) for url in (invalid_url, valid_url)]

for token in tokens:
    pprint(token)
    
min_attributes = ('scheme', 'netloc')  # add attrs to your liking
for token in tokens:
    if all(getattr(token, attr) for attr in min_attributes) is False:
        error = "'{url}' string has no scheme or netloc.".format(url=token.geturl())
        print(error)
    else:
        print("'{url}' is probably a valid url.".format(url=token.geturl()))
