def key_chain(data, *args, default=None): 
    for key in args:
        if isinstance(data, dict):
            data = data.get(key, default)
        elif isinstance(data, (list, tuple)) and isinstance(key, int):
            try:
                data = data[key]
            except IndexError:
                return default
        else:
            return default
    return data
