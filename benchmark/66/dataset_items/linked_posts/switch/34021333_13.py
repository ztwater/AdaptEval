>>> a = [partial(lambda coef, x: coef * x, coef=i) for i in (1, 2)]
>>> a[0](1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: <lambda>() got multiple values for argument 'coef'
