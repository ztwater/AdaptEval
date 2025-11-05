def chunker(iterable, size):
    if not hasattr(iterable, "__len__"):
        # generators don't have len, so fall back to slower
        # method that works with generators
        for chunk in chunker_gen(iterable, size):
            yield chunk
        return

    it = iter(iterable)
    for i in range(0, len(iterable), size):
        yield [k for k in islice(it, size)]


def chunker_gen(generator, size):
    iterator = iter(generator)
    for first in iterator:

        def chunk():
            yield first
            for more in islice(iterator, size - 1):
                yield more

        yield [k for k in chunk()]
