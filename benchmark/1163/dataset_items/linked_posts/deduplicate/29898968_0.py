>>> l = [5, 6, 6, 1, 1, 2, 2, 3, 4]
>>> reduce(lambda r, v: v in r[1] and r or (r[0].append(v) or r[1].add(v)) or r, l, ([], set()))[0]
[5, 6, 1, 2, 3, 4]
