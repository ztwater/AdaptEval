_no_pad = object()
def group(it, size, pad=_no_pad):
    if pad == _no_pad:
        it = iter(it)
        sentinel = ()
    else:
        it = chain(iter(it), repeat(pad))
        sentinel = (pad,) * size
    return iter(lambda: tuple(islice(it, size)), sentinel)
