def pop_n_elems_from_generator(g, n):
    elems = []
    try:
        for idx in xrange(0, n):
            elems.append(g.next())
        return elems
    except StopIteration:
        return elems
