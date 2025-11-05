def median(l):
    l = sorted(l)
    lent = len(l)
    if (lent % 2) == 0:
        m = int(lent / 2)
        result = l[m]
    else:
        m = int(float(lent / 2) - 0.5)
        result = l[m]
    return result
