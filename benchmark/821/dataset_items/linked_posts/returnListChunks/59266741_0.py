import itertools

def batch(iterable, size):
    it = iter(iterable)
    while item := list(itertools.islice(it, size)):
        yield item
