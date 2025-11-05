def convert(name):
    return reduce(
        lambda x, y: x + ('_' if y.isupper() else '') + y, 
        name
    ).lower()
