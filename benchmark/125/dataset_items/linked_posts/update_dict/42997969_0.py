from collections import Mapping

def update_deep(d, u):
    for k, v in u.items():
        # this condition handles the problem
        if not isinstance(d, Mapping):
            d = u
        elif isinstance(v, Mapping):
            r = update_deep(d.get(k, {}), v)
            d[k] = r
        else:
            d[k] = u[k]

    return d
