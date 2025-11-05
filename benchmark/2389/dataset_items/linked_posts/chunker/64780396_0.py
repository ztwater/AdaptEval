import more_itertools
for s in more_itertools.chunked(range(9), 4):
    print(s)
