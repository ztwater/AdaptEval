from haggis.objects import copy_func

def a(*args, **kwargs):
    """A docstring"""

a2 = copy_func(a)
a2.__doc__ = """Another docstring"""
