import itertools
def chunks2(iterable,size,filler=None):
    it = itertools.chain(iterable,itertools.repeat(filler,size-1))
    chunk = tuple(itertools.islice(it,size))
    while len(chunk) == size:
        yield chunk
        chunk = tuple(itertools.islice(it,size))

# x2, x3 and x4 could get the value 0 if the length is not
# a multiple of 4.
for x1,x2,x3,x4 in chunks2(ints,4,0):
    foo += x1 + x2 + x3 + x4
