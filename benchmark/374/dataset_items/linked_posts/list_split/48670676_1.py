def split(l, n):
    return [l[int(i*len(l)/n):int((i+1)*len(l)/n-1)] for i in range(n)]
