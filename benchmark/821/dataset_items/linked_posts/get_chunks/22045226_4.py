_no_padding = object()

def chunk(it, size, padval=_no_padding):
    if padval == _no_padding:
        it = iter(it)
        sentinel = ()
    else:
        it = chain(iter(it), repeat(padval))
        sentinel = (padval,) * size
    return iter(lambda: tuple(islice(it, size)), sentinel)
