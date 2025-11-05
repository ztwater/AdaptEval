def convert(name):
    return reduce(
        lambda x, y: x + ('_' if y.isupper() and not x.endswith('_') else '') + y, 
        name
    ).lower()
