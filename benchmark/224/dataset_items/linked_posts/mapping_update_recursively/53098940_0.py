def update(value, nvalue):
    if not isinstance(value, dict) or not isinstance(nvalue, dict):
        return nvalue
    for k, v in nvalue.items():
        value.setdefault(k, dict())
        if isinstance(v, dict):
            v = update(value[k], v)
        value[k] = v
    return value
