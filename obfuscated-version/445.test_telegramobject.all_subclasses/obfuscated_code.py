def all_subclasses(var_0):
    return set(cls.__subclasses__()).union(
        [s for c in var_0.__subclasses__() for s in all_subclasses(c)])

