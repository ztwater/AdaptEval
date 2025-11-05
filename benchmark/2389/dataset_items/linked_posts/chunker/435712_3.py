>>> from itertools import chain, izip, repeat
>>> def chunker(iterable, chunksize, fillvalue=None):
...     it   = chain(iterable, repeat(fillvalue, chunksize-1))
...     args = [it] * chunksize
...     return izip(*args)
