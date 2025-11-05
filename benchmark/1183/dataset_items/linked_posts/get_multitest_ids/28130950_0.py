class Foo:
    x = 5
    y = (lambda x=x: [x for i in range(1)])()
