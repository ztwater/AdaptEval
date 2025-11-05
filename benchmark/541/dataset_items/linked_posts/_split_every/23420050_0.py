from itertools import count, groupby
def split_every(size, iterable):
    c = count()
    for k, g in groupby(iterable, lambda x: next(c)//size):
        yield list(g) # or yield g if you want to output a generator
