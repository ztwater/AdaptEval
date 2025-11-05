def update_nested_dict(d, other):
    for k, v in other.items():
        d_v = d.get(k)
        if isinstance(v, collections.Mapping) and isinstance(d_v, collections.Mapping):
            update_nested_dict(d_v, v)
        else:
            d[k] = deepcopy(v) # or d[k] = v if you know what you're doing
