from itertools import islice, chain

def iter_in_slices(iterator, size=None):
    while True:
        slice_iter = islice(iterator, size)
        # If no first object this is how StopIteration is triggered
        peek = next(slice_iter)
        # Put the first object back and return slice
        yield chain([peek], slice_iter)
