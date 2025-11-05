from itertools import batched

flattened_data = ['roses', 'red', 'violets', 'blue', 'sugar']
unflattened = list(batched(flattened_data, 2))
assert unflattened == [('roses', 'red'), ('violets', 'blue'), ('sugar',)]
