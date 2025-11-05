from itertools import zip_longest, filterfalse

def batch_iterable(iterable, batch_size=2): 
    args = [iter(iterable)] * batch_size 
    return (tuple(filterfalse(lambda x: x is None, group)) for group in zip_longest(fillvalue=None, *args))
