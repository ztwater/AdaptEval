from itertools import tee, izip, chain

def pairwise(seq):
    a,b = tee(seq)
    next(b, None)
    return izip(a,b)

def annotated_last(seq):
    """Returns an iterable of pairs of input item and a boolean that show if
    the current item is the last item in the sequence."""
    MISSING = object()
    for current_item, next_item in pairwise(chain(seq, [MISSING])):
        yield current_item, next_item is MISSING:

for item, is_last_item in annotated_last(data_list):
    if is_last_item:
        # current item is the last item
