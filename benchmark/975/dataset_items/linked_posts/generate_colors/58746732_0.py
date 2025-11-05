import math

def calc(val, max = 16):
    if val < 1:
        return 0
    if val == 1:
        return max

    l = math.floor(math.log2(val-1))    #level 
    d = max/2**(l+1)                    #devision
    n = val-2**l                        #node
    return d*(2*n-1)
