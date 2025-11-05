    def update(orig_dict, new_dict):
        orig_dict=dict(orig_dict)
        for key, val in dict(new_dict).items():
            if isinstance(val, collections.abc.Mapping):
                tmp = update(orig_dict.get(key, { }), val)
                orig_dict[key] = tmp
            elif isinstance(val, list):
                orig_dict[key] = (orig_dict[key] + val)
            else:
                orig_dict[key] = new_dict[key]
        return orig_dict

    import collections
    import multiprocessing
    d=multiprocessing.Manager().dict({'sample':'data'})
    u={'other': 1234, "deeper": {'very': 'deep'}}

    x=update(d, u)
    x.items()
