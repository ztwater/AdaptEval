def makefunc( docstring ):
    def f():
        pass
    f.__doc__ = docstring
    return f

f = makefunc('I am f')
g = makefunc("I am f too")
