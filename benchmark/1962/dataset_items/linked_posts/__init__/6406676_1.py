@hygienic
class memoized:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kw):
        try:
            key = (tuple(args), frozenset(kw.items()))
            if not key in self.cache:
                self.cache[key] = self.func(*args,**kw)
            return self.cache[key]
        except TypeError:
            # uncacheable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args,**kw)
