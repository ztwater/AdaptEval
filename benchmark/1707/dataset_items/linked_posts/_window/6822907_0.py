from itertools import tee, izip

def window(iterable, size):
    iters = tee(iterable, size)
    for i in xrange(1, size):
        for each in iters[i:]:
            next(each, None)
    return izip(*iters)

for each in window(xrange(6), 3):
    print list(each)
