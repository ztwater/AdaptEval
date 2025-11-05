def median(array):
    if len(array) < 1:
        return(None)
    if len(array) % 2 == 0:
        median = (array[len(array)//2-1: len(array)//2+1])
        return sum(median) / len(median)
    else:
        return(array[len(array)//2])
