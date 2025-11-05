from functools import partial

def a():
    """Returns 1"""
    return 1

b = partial(a)
b.__doc__ = """Returns 1, OR DOES IT!"""

print help(a)
print help(b)
