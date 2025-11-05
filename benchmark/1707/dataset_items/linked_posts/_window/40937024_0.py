def consume(iterator, n):
    "Advance the iterator n-steps ahead. If n is none, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def window(iterable, n=2):
    "s -> (s0, ...,s(n-1)), (s1, ...,sn), (s2, ..., s(n+1)), ..."
    iters = tee(iterable, n)
    # Could use enumerate(islice(iters, 1, None), 1) to avoid consume(it, 0), but that's
    # slower for larger window sizes, while saving only small fixed "noop" cost
    for i, it in enumerate(iters):
        consume(it, i)
    return zip(*iters)
