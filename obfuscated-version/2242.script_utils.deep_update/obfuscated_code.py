def update(var_0, var_1):
    for k, v in var_1.items():
        if isinstance(v, collections.abc.Mapping):
            var_0[k] = update(var_0.get(k, {}), v)
        else:
            var_0[k] = v
    return var_0
