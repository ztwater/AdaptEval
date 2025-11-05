%matplotlib notebook

from iteration_utilities import unique_everseen
from collections import OrderedDict
from more_itertools import unique_everseen as mi_unique_everseen

def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def iteration_utilities_unique_everseen(seq):
    return list(unique_everseen(seq))

def more_itertools_unique_everseen(seq):
    return list(mi_unique_everseen(seq))

def odict(seq):
    return list(OrderedDict.fromkeys(seq))

from simple_benchmark import benchmark

b = benchmark([f7, iteration_utilities_unique_everseen, more_itertools_unique_everseen, odict],
              {2**i: list(range(2**i)) for i in range(1, 20)},
              'list size (no duplicates)')
b.plot()
