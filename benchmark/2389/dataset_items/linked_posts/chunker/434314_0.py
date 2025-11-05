import itertools
def chunks(iterable,size):
    it = iter(iterable)
    chunk = tuple(itertools.islice(it,size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it,size))

# though this will throw ValueError if the length of ints
# isn't a multiple of four:
for x1,x2,x3,x4 in chunks(ints,4):
    foo += x1 + x2 + x3 + x4

for chunk in chunks(ints,4):
    foo += sum(chunk)
