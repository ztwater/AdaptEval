from boltons import iterutils

list(iterutils.chunked_iter(list(range(50)), 11))
