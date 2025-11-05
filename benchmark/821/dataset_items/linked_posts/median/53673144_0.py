def median(alist):
    #to find median you will have to sort the list first
    sList = sorted(alist)
    first = 0
    last = len(sList)-1
    midpoint = (first + last)//2
    return midpoint
