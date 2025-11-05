from itertools import zip_longest
from functools import reduce
list(filter(lambda x: x is not None, reduce(lambda x, y: x + y, zip_longest(*data))))
