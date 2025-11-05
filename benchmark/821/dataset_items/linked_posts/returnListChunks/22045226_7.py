>>> list(chunk([1, 2, (), (), 5], 2))
[(1, 2), ((), ()), (5,)]
>>> list(chunk([1, 2, None, None, 5], 2, None))
[(1, 2), (None, None), (5, None)]
