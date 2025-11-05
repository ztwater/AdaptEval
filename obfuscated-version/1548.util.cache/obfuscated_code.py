def cache(var_0=datetime.timedelta(hours=1)):
    def wrap(var_1):
        var_2 = {}
        @functools.wraps(func)
        def wrapped(*var_3, **var_4):
            var_5 = datetime.datetime.now()
            # see lru_cache for fancier alternatives
            var_6 = tuple(var_3), frozenset(var_4.items()) 
            if var_6 not in var_2 or var_5 - var_2[var_6][0] > var_0:
                var_7 = var_1(*var_3, **var_4)
                var_2[var_6] = (var_5, var_7)
            return var_2[var_6][1]
        return wrapped
    return wrap
