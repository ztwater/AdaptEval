from collections.abc import MutableMapping as Map

def merge(d, v):
    """
    Merge two dictionaries.

    Merge dict-like `v` into dict-like `d`. In case keys between them
    are the same, merge their sub-dictionaries. Otherwise, values in  
    `v` overwrite `d`.
    """
    for key in v:
        if key in d and isinstance(d[key], Map) and isinstance(v[key], Map):
            d[key] = merge(d[key], v[key])
        else:
            d[key] = v[key]
    return d
