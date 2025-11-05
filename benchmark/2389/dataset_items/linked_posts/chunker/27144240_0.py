def chunker(iterable, size, reductor, condition):
    it = iter(iterable)
    def chunk_generator():
        return (next(it) for _ in range(size))
    chunk = reductor(chunk_generator())
    while condition(chunk):
        yield chunk
        chunk = reductor(chunk_generator())
