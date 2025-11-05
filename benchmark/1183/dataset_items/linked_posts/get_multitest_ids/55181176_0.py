import itertools as it

class Foo:
    x = 5
    y = [j for i, j in zip(range(3), it.repeat(x))]
