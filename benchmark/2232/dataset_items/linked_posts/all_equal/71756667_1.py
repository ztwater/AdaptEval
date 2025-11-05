g = itertools.groupby(s)
next(g, True) and not next(g, False)
