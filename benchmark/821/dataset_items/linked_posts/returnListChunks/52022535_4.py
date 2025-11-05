d = {}
for i, x in enumerate(iterable):
    d.setdefault(i//n, []).append(x)
    

list(d.values())
# [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10]]
