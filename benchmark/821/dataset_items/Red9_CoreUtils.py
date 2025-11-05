import re

def sorted_nicely(items):
    """
    Sort the given iterable in the way that humans expect.
    """

    # taken form: https://stackoverflow.com/questions/2669059/how-to-sort-alpha-numeric-set-in-python
    # From Mark Byers https://stackoverflow.com/users/61974/mark-byers

    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(items, key = alphanum_key)
