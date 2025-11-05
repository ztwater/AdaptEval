def grouper(n, iter_or_seq):
    if hasattr(iter_or_seq, "__getslice__"):
        return slice_grouper(n, iter_or_seq)
    elif hasattr(iter_or_seq, "__iter__"):
        return iter_grouper(n, iter_or_seq)
