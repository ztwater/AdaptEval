class Foo:
    x = 5
    y = [j for j in (x,) for i in range(3)]
