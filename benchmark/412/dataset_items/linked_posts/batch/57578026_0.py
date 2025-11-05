def batch(iterable, n):
    iterable=iter(iterable)
    while True:
        chunk=[]
        for i in range(n):
            try:
                chunk.append(next(iterable))
            except StopIteration:
                yield chunk
                return
        yield chunk

list(batch(range(10), 3))
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
