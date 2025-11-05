def merge_dict(var_0, var_1):
    for key, val in var_0.items():
        if type(val) == dict:
            if key in var_1 and type(var_1[key] == dict):
                merge_dict(var_0[key], var_1[key])
        else:
            if key in var_1:
                var_0[key] = var_1[key]

    for key, val in var_1.items():
        if not key in var_0:
            var_0[key] = val

    return var_0