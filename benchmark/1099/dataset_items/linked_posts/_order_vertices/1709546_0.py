>>> import math
>>> mlat = sum(x['lat'] for x in l) / len(l)
>>> mlng = sum(x['lng'] for x in l) / len(l)
>>> def algo(x):
    return (math.atan2(x['lat'] - mlat, x['lng'] - mlng) + 2 * math.pi) % (2*math.pi)

>>> l.sort(key=algo)
