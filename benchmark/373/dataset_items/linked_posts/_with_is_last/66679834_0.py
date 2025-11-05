def rev_enumerate(lst):
    """
    Similar to enumerate(), but counts DOWN to the last element being the
    zeroth, rather than counting UP from the first element being the zeroth.

    Since the length has to be determined up-front, this is not suitable for
    open-ended iterators.

    Parameters
    ----------
    lst : Iterable
        An iterable with a length (list, tuple, dict, set).

    Yields
    ------
    tuple
        A tuple with the reverse cardinal number of the element, followed by
        the element of the iterable.
    """
    length = len(lst) - 1
    for i, element in enumerate(lst):
        yield length - i, element
