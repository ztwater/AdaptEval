def time_elapsed(etime):
    # need to add tzinfo to datetime.utcnow
    now = datetime.utcnow().replace(tzinfo=etime.tzinfo)
    opened_for = (now - etime).total_seconds()
    names = ["seconds","minutes","hours","days","weeks","months"]
    modulos = [ 1,60,3600,3600*24,3600*24*7,3660*24*30]
    values = []
    for m in modulos[::-1]:
        values.append(int(opened_for / m))
        opened_for -= values[-1]*m
    pretty = [] 
    for i,nm in enumerate(names[::-1]):
        if values[i]!=0:
            pretty.append("%i %s" % (values[i],nm))
    return " ".join(pretty)
