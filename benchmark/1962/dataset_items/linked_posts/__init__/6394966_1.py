@class_wraps
class memoized:
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """

    def __init__(self, func):
        super().__init__()
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncacheable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __get__(self, obj, objtype):
        return functools.partial(self.__call__, obj)


@memoized
def fibonacci(n):
    """fibonacci docstring"""
    if n in (0, 1):
       return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci)
print("__doc__: ", fibonacci.__doc__)
print("__name__: ", fibonacci.__name__)
