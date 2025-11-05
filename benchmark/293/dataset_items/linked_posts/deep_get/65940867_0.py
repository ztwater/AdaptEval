In [1]: from glom import glom

In [2]: data = {'a': {'b': {'c': 'd'}}}

In [3]: glom(data, "a.b.c")
Out[3]: 'd'
