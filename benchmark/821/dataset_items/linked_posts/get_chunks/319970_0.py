def chunk(lst):
    out = []
    for x in xrange(2, len(lst) + 1):
        if not len(lst) % x:
            factor = len(lst) / x
            break
    while lst:
        out.append([lst.pop(0) for x in xrange(factor)])
    return out
