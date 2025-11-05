def components(path):
    ret = []
    while len(path) > 0:
        path, crust = split(path)
        ret.insert(0, crust)
    return ret
