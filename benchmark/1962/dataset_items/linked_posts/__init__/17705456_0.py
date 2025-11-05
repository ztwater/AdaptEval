>>> import functools
>>> class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, func):
        self.func = func
        self.cache = {}
        functools.update_wrapper(self, func)  ## TA-DA! ##
    def __call__(self, *args):
        pass  # Not needed for this demo.

>>> @memoized
def fibonacci(n):
    """fibonacci docstring"""
    pass  # Not needed for this demo.

>>> fibonacci
<__main__.memoized object at 0x0156DE30>
>>> fibonacci.__name__
'fibonacci'
>>> fibonacci.__doc__
'fibonacci docstring'
