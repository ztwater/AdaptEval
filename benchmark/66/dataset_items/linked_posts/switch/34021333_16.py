>>> a = [lambda x, coef=i: coef * x for i in (1, 2)]
>>> a[0](2), a[1](2)
(2, 4)
