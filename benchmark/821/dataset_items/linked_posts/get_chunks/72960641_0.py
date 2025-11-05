def chunkify(lst, n):
    for tup in zip(*[iter(lst)]*n):
        yield tup
    rest = tuple(lst[len(lst)//n*n: ])
    if rest:
        yield rest

list(chunkify(range(7), 3)) # [(0, 1, 2), (3, 4, 5), (6,)]
