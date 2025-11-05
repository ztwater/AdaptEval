import random

b = benchmark([f7, iteration_utilities_unique_everseen, more_itertools_unique_everseen, odict],
              {2**i: [random.randint(0, 2**(i-1)) for _ in range(2**i)] for i in range(1, 20)},
              'list size (lots of duplicates)')
b.plot()
