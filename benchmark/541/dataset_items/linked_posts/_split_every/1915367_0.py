from itertools import *
def iter_grouper(n, iterable):
    it = iter(iterable)
    item = itertools.islice(it, n)
    while item:
        yield item
        item = itertools.islice(it, n)
