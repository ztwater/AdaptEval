def split_every(n, iterable):
    iterable = iter(iterable)
    for chunk in iter(lambda: list(islice(iterable, n)), []):
        yield chunk
