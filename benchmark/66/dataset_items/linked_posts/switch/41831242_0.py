import functools
a = [functools.partial(lambda x: x*x, x) for x in range(10)]

b = []
for i in a:
    b.append(i())

In [26]: b
Out[26]: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
