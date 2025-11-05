import itertools
def split_groups(iter_in, group_size):
    return ((x for _, x in item) for _, item in itertools.groupby(enumerate(iter_in), key=lambda x: x[0] // group_size))

for x, y, z, w in split_groups(range(16), 4):
    foo += x * y + z * w
