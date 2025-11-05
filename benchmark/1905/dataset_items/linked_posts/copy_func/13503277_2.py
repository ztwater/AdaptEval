import types
import functools
def copy_func(f):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.func_code, f.func_globals, name=f.func_name,
                           argdefs=f.func_defaults,
                           closure=f.func_closure)
    g = functools.update_wrapper(g, f)
    return g

def f(x, y=2):
    return x,y
f.cache = [1,2,3]
g = copy_func(f)

print(f(1))
print(g(1))
print(g.cache)
assert f is not g
