from pprint import pprint

items = list(range(10, 75))
pprint(cycle_baskets(items, 10))
pprint(slice_baskets(items, 10))
pprint([list(s) for s in yield_islice_baskets(items, 10)])
