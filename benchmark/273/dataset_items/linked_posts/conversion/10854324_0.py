# -*- coding: latin-1 -*-

def conversion(old):
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ')
    new = new.split()
    new_dir = new.pop()
    new.extend([0,0,0])
    return (int(new[0])+int(new[1])/60.0+int(new[2])/3600.0) * direction[new_dir]

lat, lon = u'''0°25'30"S, 91°7'W'''.split(', ')
print conversion(lat), conversion(lon)
#Output:
0.425 91.1166666667
