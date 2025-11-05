def recursively_update_dict(d: dict, u: dict):
    for k, v in u.items():
        if isinstance(v, dict):
            d.setdefault(k, {})
            recursively_update_dict(d[k], v)
        else:
            d[k] = v
