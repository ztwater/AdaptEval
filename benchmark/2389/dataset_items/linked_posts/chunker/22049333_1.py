from itertools import islice, chain, repeat

def group_pad(it, size, pad=None):
    it = chain(iter(it), repeat(pad))
    return iter(lambda: tuple(islice(it, size)), (pad,) * size)
