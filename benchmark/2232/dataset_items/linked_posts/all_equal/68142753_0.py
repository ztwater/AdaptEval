def all_eq(lst):
    for idx, itm in enumerate(lst):
        if not idx:   # == 0
            prev = itm
        if itm != prev:
            return False
        prev = itm
    return True
