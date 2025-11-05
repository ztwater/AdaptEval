from itertools import izip_longest

import numpy as np

def grouper(n, iterable, fillvalue=None): # This is grouper from itertools
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def another_chunk(x,num):
    extra_ele = len(x)%num #gives number of parts that will have an extra element 
    small_part = int(np.floor(len(x)/num)) #gives number of elements in a small part

    new_x = list(grouper(small_part,x[:small_part*(num-extra_ele)]))
    new_x.extend(list(grouper(small_part+1,x[small_part*(num-extra_ele):])))

    return new_x
