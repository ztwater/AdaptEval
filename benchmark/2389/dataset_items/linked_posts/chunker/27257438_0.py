def chunker(iterable, chunksize):
    return zip(*[iter(iterable)]*chunksize)
