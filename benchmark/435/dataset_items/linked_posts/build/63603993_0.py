from typing import List
import math
def kernels(ind,outd) -> List:
    """Returns a List [(kernel_offset_start,kernel_length)] defining all the pooling kernels for a 1-D adaptive pooling layer that takes an input of dimension `ind` and yields an output of dimension `outd`"""
    def start_index(a,b,c):
        return math.floor((float(a) * float(c)) / b)
    def end_index(a,b,c):
        return math.ceil((float(a + 1) * float(c)) / b)
    results = []
    for ow in range(outd):
        start = start_index(ow,outd,ind)
        end = end_index(ow,outd,ind)
        sz = end - start
        results.append((start,sz))
    return results

def kernel_indexes(ind,out) -> List:
    """Returns a List [[*ind]] containing the indexes of the pooling kernels"""
    startsLengths = kernels(ind,out)
    return [list(range(start,start+length)) for (start,length) in startsLengths]
