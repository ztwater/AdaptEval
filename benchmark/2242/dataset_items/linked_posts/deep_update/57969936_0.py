def update_nested(dict_a, dict_b):
    set_keys = set(dict_a.keys()).union(set(dict_b.keys()))
    for k in set_keys:
        v = dict_a.get(k)
        if isinstance(v, dict):
            new_dict = dict_b.get(k, None)
            if new_dict:
                update_nested(v, new_dict)
        else:
            new_value = dict_b.get(k, None)
            if new_value:
                dict_a[k] = new_value
