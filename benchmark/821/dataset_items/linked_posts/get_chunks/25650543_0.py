def nChunks(l, n):
    """ Yield n successive chunks from l.
    Works for lists,  pandas dataframes, etc
    """
    newn = int(1.0 * len(l) / n + 0.5)
    for i in xrange(0, n-1):
        yield l[i*newn:i*newn+newn]
    yield l[n*newn-newn:]
