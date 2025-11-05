>>> from functools import partial
>>> a = [partial(lambda y, x: y * x, i) for i in (1, 2)]
>>> a[0](2), a[1](2)
(2, 4)
