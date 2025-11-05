from pandas import DataFrame, MultiIndex
from itertools import product

index = range(2), range(2), range(2)
value = range(2 * 2 * 2)
frame = DataFrame(value, columns=['value'],
                  index=MultiIndex.from_product(index)).drop((1, 0, 1))
print(frame)
