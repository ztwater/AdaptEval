def group_by(iterable, size):
    """Group an iterable into lists that don't exceed the size given.

    >>> group_by([1,2,3,4,5], 2)
    [[1, 2], [3, 4], [5]]

    """
    sublist = []

    for index, item in enumerate(iterable):
        if index > 0 and index % size == 0:
            yield sublist
            sublist = []

        sublist.append(item)

    if sublist:
        yield sublist
