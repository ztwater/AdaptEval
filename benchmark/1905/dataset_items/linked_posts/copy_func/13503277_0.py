import types
import functools

def copy_func(f):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                           argdefs=f.__defaults__,
                           closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g

def f(arg1, arg2, arg3, kwarg1="FOO", *args, kwarg2="BAR", kwarg3="BAZ"):
    return (arg1, arg2, arg3, args, kwarg1, kwarg2, kwarg3)
f.cache = [1,2,3]
g = copy_func(f)

print(f(1,2,3,4,5))
print(g(1,2,3,4,5))
print(g.cache)
assert f is not g
