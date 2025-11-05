"""Utilities."""
  
def isnamedtupleinstance(x):
    """From https://stackoverflow.com/a/2166841/6067848"""
    t = type(x)
    b = t.__bases__
    if len(b) != 1 or b[0] != tuple:
        return False

    f = getattr(t, "_fields", None)
    if not isinstance(f, tuple):
        return False

    return all(isinstance(n, str) for n in f)

 