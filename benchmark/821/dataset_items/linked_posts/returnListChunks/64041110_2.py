def chunk_iters(it, n):
    cit = iter(it)
    def one_chunk(f):
        yield f
        for i, e in zip(range(n - 1), cit):
            yield e
    for f in cit:
        yield one_chunk(f)
