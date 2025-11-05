def chunks_gen_sentinel(n, seq):
    continuous_slices = imap(islice, repeat(iter(seq)), repeat(0), repeat(n))
    return iter(imap(tuple, continuous_slices).next,())
