def from_filesize(spec, si=True):
    decade = 1000 if si else 1024
    suffixes = tuple('BKMGTP')

    num = float(spec[:-1])
    s = spec[-1]
    i = suffixes.index(s)

    for n in range(i):
        num *= decade

    return int(num)
