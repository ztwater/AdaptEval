seen = set()
[x for x in seq if not (x in seen or seen.add(x))]
