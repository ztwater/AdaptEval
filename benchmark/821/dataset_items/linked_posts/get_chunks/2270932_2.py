def isplitter2(l, n):
    return takewhile(bool,
                     (tuple(islice(start, n))
                            for start in repeat(iter(l))))
