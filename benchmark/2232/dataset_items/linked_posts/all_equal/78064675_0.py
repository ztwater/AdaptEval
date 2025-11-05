from itertools import groupby, pairwise

def all_equal(iterable):
    return not any(pairwise(groupby(iterable)))
