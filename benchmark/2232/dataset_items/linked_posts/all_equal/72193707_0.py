def all_equal(iterable):
    g = groupby(iterable)
    return not any(g) or not any(g)

def all_equal(iterable):
    g = groupby(iterable)
    next(g, None)
    return not next(g, False)

def all_equal(iterable):
    g = groupby(iterable)
    return not next(g, False) or not next(g, False)
