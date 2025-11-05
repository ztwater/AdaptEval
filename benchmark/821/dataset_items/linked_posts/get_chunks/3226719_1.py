def chunks(L, n): return [L[x: x+n] for x in xrange(0, len(L), n)]
chunks(L, 10)
