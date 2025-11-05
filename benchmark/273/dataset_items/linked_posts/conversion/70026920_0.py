def dec(coord):
    c = coord.upper()
    s = 1
    if c.find('S')>0 or c.find('W')>0:
        s = -1
    c = c.replace('N','').replace('E','').replace('S','').replace('W','').replace(',','.').replace(u'°',' ').replace('\'',' ').replace('"',' ')
    a = c.split()
    a.extend([0,0,0])
    try:
        return s*(float(a[0])+float(a[1])/60.0+float(a[2])/3600.0) 
    except:
        return coord
