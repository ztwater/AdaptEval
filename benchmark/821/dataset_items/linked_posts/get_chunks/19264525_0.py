from itertools import islice

def chunks(n, iterable):
    iterable = iter(iterable)
    while True:
        yield tuple(islice(iterable, n)) or iterable.next()
