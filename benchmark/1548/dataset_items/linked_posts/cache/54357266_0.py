import cachetools.func

@cachetools.func.ttl_cache(maxsize=128, ttl=10 * 60)
def example_function(key):
    return get_expensively_computed_value(key)


class ExampleClass:
    EXP = 2

    @classmethod
    @cachetools.func.ttl_cache()
    def example_classmethod(cls, i):
        return i* cls.EXP

    @staticmethod
    @cachetools.func.ttl_cache()
    def example_staticmethod(i):
        return i * 3
