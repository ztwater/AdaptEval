def allTheSame(i):
    j = itertools.groupby(i)
    for k in j: break
    for k in j: return False
    return True
