>>> class Foo:
...     x = 5
...     def y(x):
...         return [x for i in range(1)]
...     y = y(x)
... 
>>> Foo.y
[5]
