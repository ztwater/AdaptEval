>>> a = [partial(lambda x, coef: coef * x, coef=i) for i in (1, 2)]
>>> a[0](2), a[1](2)
(2, 4)
