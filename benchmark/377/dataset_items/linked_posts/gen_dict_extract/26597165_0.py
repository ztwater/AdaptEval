def find_all_items(obj, key, keys=None):
    """
    Example of use:
    d = {'a': 1, 'b': 2, 'c': {'a': 3, 'd': 4, 'e': {'a': 9, 'b': 3}, 'j': {'c': 4}}}
    for k, v in find_all_items(d, 'a'):
        print "* {} = {} *".format('->'.join(k), v)    
    """
    ret = []
    if not keys:
        keys = []
    if key in obj:
        out_keys = keys + [key]
        ret.append((out_keys, obj[key]))
    for k, v in obj.items():
        if isinstance(v, dict):
            found_items = find_all_items(v, key, keys=(keys+[k]))
            ret += found_items
    return ret
