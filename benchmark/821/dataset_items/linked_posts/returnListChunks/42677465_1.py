    return [list(it) for _, it in itertools.groupby(l, lambda x: next(c)//n)]
