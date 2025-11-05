def all_equal_in_iterable(iterable: Iterable):
    iterable = list(iterable)
    if not iterable:
        return True
    return all(item == iterable[0] for item in iterable)
