def erat3( ):
    from itertools import islice, count

    # q is the running integer that's checked for primeness.
    # yield 2 and no other even number thereafter
    yield 2
    D = {}
    # no need to mark D[4] as we will test odd numbers only
    for q in islice(count(3),0,None,2):
        if q in D:                  #  is composite
            p = D[q]
            del D[q]
            # q is composite. p=D[q] is the first prime that
            # divides it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiple of its witnesses to prepare for larger
            # numbers.
            x = q + p+p        # next odd(!) multiple
            while x in D:      # skip composites
                x += p+p
            D[x] = p
        else:                  # is prime
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations.
            D[q*q] = q
            yield q
