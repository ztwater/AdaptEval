def mark_last(iterable):
    try:
        *init, last = iterable
    except ValueError:  # if iterable is empty
        return

    for e in init:
        yield e, True
    yield last, False
