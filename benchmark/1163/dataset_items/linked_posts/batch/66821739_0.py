def get_value_from_path(dictionary, parts):
    """ extracts a value from a dictionary using a dotted path string """

    if type(parts) is str:
        parts = parts.split('.')

    if len(parts) > 1:
        return get_value_from_path(dictionary[parts[0]], parts[1:])

    return dictionary[parts[0]]

a = {'a':{'b':'c'}}
print(get_value_from_path(a, 'a.b')) # c
