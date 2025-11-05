def outerzip(*args):
    # args = (a, default_a), (b, default_b), ...
    max_length = max( map( lambda s: len(s[0]), args))
    extended_args = [ s[0] + [s[1]]*(max_length-len(s[0])) for s in args ]
    return zip(*extended_args)

outerzip((a, 0), (b, 1)) # [(1, 4), (2, 5), (3, 6), (0, 7)]
