def chunks(iterable, size):
    """
    Yield successive chunks from iterable, being `size` long.

    https://stackoverflow.com/a/55776536/3423324
    :param iterable: The object you want to split into pieces.
    :param size: The size each of the resulting pieces should have.
    """
    i = 0
    while True:
        sliced = iterable[i:i + size]
        if len(sliced) == 0:
            # to suppress stuff like `range(max, max)`.
            break
        # end if
        yield sliced
        if len(sliced) < size:
            # our slice is not the full length, so we must have passed the end of the iterator
            break
        # end if
        i += size  # so we start the next chunk at the right place.
    # end while
# end def
