def dms(deg):
    f,d = math.modf(deg)
    s,m = math.modf(abs(f) * 60)
    return (d,m,s * 60)
