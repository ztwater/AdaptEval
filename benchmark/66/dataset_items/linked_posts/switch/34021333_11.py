>>> a = [(lambda y: (lambda x: y * x))(i) for i in (1, 2)]
>>> a[1](1)
2
>>> a[0](1)
1
