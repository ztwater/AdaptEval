from itertools import starmap, pairwise
all(starmap(eq, (pairwise(x)))
