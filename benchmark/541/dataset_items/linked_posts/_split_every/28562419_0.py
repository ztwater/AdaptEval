import itertools
def split_groups(iter_in, group_size):
     return ((x for _, x in item) for _, item in itertools.groupby(enumerate(iter_in), key=lambda x: x[0] // group_size))
