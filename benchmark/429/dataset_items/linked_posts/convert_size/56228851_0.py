from bisect import bisect

def to_filesize(bytes_num, si=True):
    decade = 1000 if si else 1024
    partitions = tuple(decade ** n for n in range(1, 6))
    suffixes = tuple('BKMGTP')

    i = bisect(partitions, bytes_num)
    s = suffixes[i]

    for n in range(i):
        bytes_num /= decade

    f = '{:.3f}'.format(bytes_num)

    return '{}{}'.format(f.rstrip('0').rstrip('.'), s)
