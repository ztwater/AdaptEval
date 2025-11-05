def chunks(iterable, n):
    """Yield successive n-sized chunks from iterable."""
    values = []
    for i, item in enumerate(iterable, 1):
        values.append(item)
        if i % n == 0:
            yield values
            values = []
    if values:
        yield values
