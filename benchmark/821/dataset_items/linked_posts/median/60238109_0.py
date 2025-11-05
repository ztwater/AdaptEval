def median(d):
    d=np.sort(d)
    n2=int(len(d)/2)
    r=n2%2
    if (r==0):
        med=d[n2] 
    else:
        med=(d[n2] + d[n2+1]) / 2
    return med
