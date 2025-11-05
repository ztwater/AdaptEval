import collections

def update(var_0, var_1):
    for k, v in var_1.iteritems():
        if isinstance(v, collections.Mapping):
            var_0[k] = update(var_0.get(k, {}), v)
        else:
            var_0[k] = v
    return var_0
