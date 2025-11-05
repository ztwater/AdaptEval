import itertools as it
def window(iterable, size):
    shiftedStarts = [it.islice(iterable, s, None) for s in xrange(size)]
    return it.izip(*shiftedStarts)
