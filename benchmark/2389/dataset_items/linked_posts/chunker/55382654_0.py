def chunks(it, n, m):
    """Make an iterator over m first chunks of size n.
    """
    it = iter(it)
    # Chunks are presented as tuples.
    return (tuple(next(it) for _ in range(n)) for _ in range(m))
