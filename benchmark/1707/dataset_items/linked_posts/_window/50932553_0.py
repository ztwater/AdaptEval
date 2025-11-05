import itertools
def window(seq, n=2,step=1,fill=None,keep=0):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(itertools.islice(it, n))    
    if len(result) == n:
        yield result
    while True:        
#         for elem in it:        
        elem = tuple( next(it, fill) for _ in range(step))
        result = result[step:] + elem        
        if elem[-1] is fill:
            if keep:
                yield result
            break
        yield result
