import functools
a = [functools.partial(lambda x: print(x), x) for x in range(10)]

for i in a:
    i()
