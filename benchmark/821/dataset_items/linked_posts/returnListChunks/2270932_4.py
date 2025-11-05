def chunks_gen_filter(n, seq):
    continuous_slices = imap(islice, repeat(iter(seq)), repeat(0), repeat(n))
    return takewhile(bool,imap(tuple, continuous_slices))
