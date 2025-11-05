from itertools import izip_longest

def chunker(iterable, chunksize, filler):
    return izip_longest(*[iter(iterable)]*chunksize, fillvalue=filler)
