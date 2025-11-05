def grouper(n, iterable, fillvalue=None):
    #"grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    # itertools.zip_longest on Python 3
    for x in itertools.izip_longest(*args, fillvalue=fillvalue):
        if x[-1] is fillvalue:
            yield tuple(v for v in x if v is not fillvalue)
        else:
            yield x
