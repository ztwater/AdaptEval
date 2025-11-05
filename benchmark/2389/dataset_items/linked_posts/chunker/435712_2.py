>>> from itertools import izip
>>> def chunker(iterable, chunksize):
...     return izip(*[iter(iterable)]*chunksize)
