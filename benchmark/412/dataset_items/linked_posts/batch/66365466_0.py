from itertools import islice

def chunked(generator, size):
    """Read parts of the generator, pause each time after a chunk"""
    # islice returns results until 'size',
    # make_chunk gets repeatedly called by iter(callable).
    gen = iter(generator)
    make_chunk = lambda: list(islice(gen, size))
    return iter(make_chunk, [])
