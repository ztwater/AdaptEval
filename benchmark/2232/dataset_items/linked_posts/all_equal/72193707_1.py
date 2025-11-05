def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)
