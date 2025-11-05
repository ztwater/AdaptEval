def chunker(seq, size):
    res = []
    for el in seq:
        res.append(el)
        if len(res) == size:
            yield res
            res = []
    if res:
        res = res + (size - len(res)) * [res[-1]] 
        yield res
