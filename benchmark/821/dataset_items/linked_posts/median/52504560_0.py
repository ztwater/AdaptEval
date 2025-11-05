def median(x):
    x = sorted(x)
    listlength = len(x) 
    num = listlength//2
    if listlength%2==0:
        middlenum = (x[num]+x[num-1])/2
    else:
        middlenum = x[num]
    return middlenum
