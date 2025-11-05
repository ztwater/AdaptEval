>>> def chunker(iterable, chunksize):
...   return map(None,*[iter(iterable)]*chunksize)
