def chunked(iterable, size):
    stop = []
    it = iter(iterable)
    def _next_chunk():
        try:
            for _ in xrange(size):
                yield next(it)
        except StopIteration:
            stop.append(True)
            return

    while not stop:
        yield _next_chunk()

for it in chunked(xrange(16), 4):
   print list(it)
