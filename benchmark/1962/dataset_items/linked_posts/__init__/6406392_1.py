class memoized(CallableClassDecorator):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
    def __init__(self, function):
        super().__init__(function)
        self.function = function
        self.cache = {}

    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.function(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncacheable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.function(*args)
