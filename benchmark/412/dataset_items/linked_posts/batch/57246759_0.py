def chunks(iterable, size):
    from itertools import chain, islice
    iterator = iter(iterable)
    for first in iterator:
        yield list(chain([first], islice(iterator, size - 1)))
