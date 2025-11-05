def chunks(l, n):
    c = itertools.count()
    return (it for _, it in itertools.groupby(l, lambda x: next(c)//n))
