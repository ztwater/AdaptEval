def chunk_iter(iterable, chunk_size):
it = iter(iterable)
while True:
    chunk = tuple(next(it) for _ in range(chunk_size))
    if not chunk:
        break
    yield chunk
