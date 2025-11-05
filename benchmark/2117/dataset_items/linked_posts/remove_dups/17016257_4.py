seen = set()
[x for x in seq if x not in seen and not seen.add(x)]
