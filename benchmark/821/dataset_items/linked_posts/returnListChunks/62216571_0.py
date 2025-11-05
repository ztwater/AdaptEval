from enum import Enum

class PartialChunkOptions(Enum):
    INCLUDE = 0
    EXCLUDE = 1
    PAD = 2
    ERROR = 3

class PartialChunkException(Exception):
    pass

def chunker(iterable, n, on_partial=PartialChunkOptions.INCLUDE, pad=None):
    """
    A chunker yielding n-element lists from an iterable, with various options
    about what to do about a partial chunk at the end.

    on_partial=PartialChunkOptions.INCLUDE (the default):
                     include the partial chunk as a short (<n) element list

    on_partial=PartialChunkOptions.EXCLUDE
                     do not include the partial chunk

    on_partial=PartialChunkOptions.PAD
                     pad to an n-element list 
                     (also pass pad=<pad_value>, default None)

    on_partial=PartialChunkOptions.ERROR
                     raise a RuntimeError if a partial chunk is encountered
    """

    on_partial = PartialChunkOptions(on_partial)        

    iterator = iter(iterable)
    while True:
        vals = []
        for i in range(n):
            try:
                vals.append(next(iterator))
            except StopIteration:
                if vals:
                    if on_partial == PartialChunkOptions.INCLUDE:
                        yield vals
                    elif on_partial == PartialChunkOptions.EXCLUDE:
                        pass
                    elif on_partial == PartialChunkOptions.PAD:
                        yield vals + [pad] * (n - len(vals))
                    elif on_partial == PartialChunkOptions.ERROR:
                        raise PartialChunkException
                    return
                return
        yield vals
