def safe_get(dictionary, *keys, default=None):
    for key in keys:
        if key not in dictionary:
            return default
        dictionary = dictionary[key]
    return dictionary
