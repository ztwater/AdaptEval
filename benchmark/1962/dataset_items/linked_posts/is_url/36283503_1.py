from urllib.parse import urlparse

min_attributes = ('scheme', 'netloc')


def is_valid(url, qualifying=min_attributes):
    tokens = urlparse(url)
    return all(getattr(tokens, qualifying_attr)
               for qualifying_attr in qualifying)
