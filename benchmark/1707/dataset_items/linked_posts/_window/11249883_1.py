import itertools as it
def window(iterable, size):
    itrs = it.tee(iterable, size)
    shiftedStarts = [it.islice(anItr, s, None) for s, anItr in enumerate(itrs)]
    return it.izip(*shiftedStarts)
