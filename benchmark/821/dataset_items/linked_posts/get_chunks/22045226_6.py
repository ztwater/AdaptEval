_no_padding = object()
def chunk(it, size, padval=_no_padding):
    it = iter(it)
    chunker = iter(lambda: tuple(islice(it, size)), ())
    if padval == _no_padding:
        yield from chunker
    else:
        for ch in chunker:
            yield ch if len(ch) == size else ch + (padval,) * (size - len(ch))
