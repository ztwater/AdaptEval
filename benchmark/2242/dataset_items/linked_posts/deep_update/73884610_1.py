from collections import defaultdict

def recursively_update_defaultdict(d: defaultdict[dict], u: dict):
    for k, v in u.items():
        if isinstance(v, dict):
            recursively_update_dict(d[k], v)
        else:
            d[k] = v
