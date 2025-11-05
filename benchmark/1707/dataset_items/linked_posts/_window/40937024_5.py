def windowkindalltupled(iterable, n=2, tuple=tuple):
    it = iter(iterable)
    win = deque(islice(it, n), n)
    if len(win) < n:
        return
    append = win.append
    yield tuple(win)
    for e in it:
        append(e)
        yield tuple(win)
