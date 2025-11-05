#from itertools import izip_longest as zip_longest # for Python 2.x
from itertools import zip_longest # for Python 3.x
#from six.moves import zip_longest # for both (uses the six compat library)

def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)
