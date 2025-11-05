def chunks(l, n):
    """ Yield n successive chunks from l.
    """
    newn = int(len(l) / n)
    for i in xrange(0, n-1):
        yield l[i*newn:i*newn+newn]
    yield l[n*newn-newn:]

l = range(56)
three_chunks = chunks (l, 3)
print three_chunks.next()
print three_chunks.next()
print three_chunks.next()
