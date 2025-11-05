#!/usr/bin/env python3
from itertools import zip_longest


_UNDEFINED = object()


def chunker(iterable, chunksize, fillvalue=_UNDEFINED):
    """
    Collect data into chunks and optionally pad it.

    Performance worsens as `chunksize` approaches 1.

    Inspired by:
        https://docs.python.org/3/library/itertools.html#itertools-recipes

    """
    args = [iter(iterable)] * chunksize
    chunks = zip_longest(*args, fillvalue=fillvalue)
    yield from (
        filter(lambda val: val is not _UNDEFINED, chunk)
        if chunk[-1] is _UNDEFINED
        else chunk
        for chunk in chunks
    ) if fillvalue is _UNDEFINED else chunks
