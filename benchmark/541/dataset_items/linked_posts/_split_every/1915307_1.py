>>> list(split_every(5, range(9)))
[[0, 1, 2, 3, 4], [5, 6, 7, 8]]

>>> list(split_every(3, (x**2 for x in range(20))))
[[0, 1, 4], [9, 16, 25], [36, 49, 64], [81, 100, 121], [144, 169, 196], [225, 256, 289], [324, 361]]

>>> [''.join(s) for s in split_every(6, 'Hello world')]
['Hello ', 'world']

>>> list(split_every(100, []))
[]
