def all_equal_ivo(lst):
    return not lst or lst.count(lst[0]) == len(lst)
