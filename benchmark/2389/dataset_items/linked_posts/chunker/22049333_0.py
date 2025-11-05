from itertools import islice

def group(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())
