def batch(size, i):
    """ Get the i'th batch of the given size """
    return slice(size* i, size* i + size)
