def is_json(obj: object):
    return obj is None or type(obj) in {bool, int, str, list, dict}

def attrs(obj: object):
    return {
        name: getattr(obj, name)
        for name in dir(obj)
    }

def props(obj: object, max_depth: int=1, depth: int=0):
    if depth > max_depth:
        return {}

    return {
        name: attr if is_json(attr) else props(attr, max_depth, depth+1)
        for name, attr in attrs(obj).items()
        if not name.startswith('__') and not callable(attr)
    }
