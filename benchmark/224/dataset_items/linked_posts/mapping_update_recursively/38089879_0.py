def update_dict(d, u):
    for k, v in u.items():
        if isinstance(v, collections.Mapping):
            default = v.copy()
            default.clear()
            r = update_dict(d.get(k, default), v)
            d[k] = r
        else:
            d[k] = v
    return d
