def all_identical(seq):
    if not seq:
        # empty list is False.
        return False
    first = seq[0]
    return all(first == elem for elem in seq)
