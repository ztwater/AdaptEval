def from_camel(name):
    """
    ThisIsCamelCase ==> this_is_camel_case
    """
    name = name.replace("_", "")
    _cas = lambda _x : [_i.isupper() for _i in _x]
    seq = zip(_cas(name[1:-1]), _cas(name[2:]))
    ss = [_x + 1 for _x, (_i, _j) in enumerate(seq) if (_i, _j) == (False, True)]
    return "".join([ch + "_" if _x in ss else ch for _x, ch in numerate(name.lower())])
