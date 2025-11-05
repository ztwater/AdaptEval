def split(what, target_length=79):
    '''splits list of strings into sublists, each 
    having string length at most 79'''
    out = [[]]
    while what:
        if len("', '".join(out[-1])) + len(what[0]) < target_length:
            out[-1].append(what.pop(0))
        else:
            if not out[-1]: # string longer than target_length
                out[-1] = [what.pop(0)]
            out.append([])
    return out
