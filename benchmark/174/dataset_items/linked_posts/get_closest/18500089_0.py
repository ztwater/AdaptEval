def find_nearest(array, value):
    n = [abs(i-value) for i in array]
    idx = n.index(min(n))
    return array[idx]
