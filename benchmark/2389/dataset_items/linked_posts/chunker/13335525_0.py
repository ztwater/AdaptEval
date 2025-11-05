def chunkiter(iterable, size):
  def inneriter(first, iterator, size):
    yield first
    for _ in xrange(size - 1): 
      yield iterator.next()
  it = iter(iterable)
  while True:
    yield inneriter(it.next(), it, size)

In [2]: i = chunkiter('abcdefgh', 3)
In [3]: for ii in i:                                                
          for c in ii:
            print c,
          print ''
        ...:     
        a b c 
        d e f 
        g h 
