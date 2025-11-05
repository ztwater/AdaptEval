def chunk(input, size):
    return map(None, *([iter(input)] * size))
