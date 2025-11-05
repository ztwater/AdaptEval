def unique(lst):
    return [] if lst==[] else [lst[0]] + unique(filter(lambda x: x!= lst[0], lst[1:]))
