def chunks(seq, size):
    it = iter(seq)
    while True:
        ret = tuple(next(it) for _ in range(size))
        if len(ret) == size:
            yield ret
        else:
            raise StopIteration()
