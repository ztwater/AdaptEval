import math
 
def chunk(lst, n):
    chunk_size = math.ceil(len(lst) / n)
    return [lst[i: min(i+chunk_size, len(lst))] for i in range(0, len(lst), chunk_size)]
