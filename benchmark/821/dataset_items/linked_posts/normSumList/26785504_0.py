def normalize(lst):
    s = sum(lst)
    return map(lambda x: float(x)/s, lst)
