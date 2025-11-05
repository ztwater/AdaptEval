from itertools import combinations
from math import sqrt

coords = [{'lat': 39.7612992 , 'lon': -86.1519681}, 
                {"lat": 39.762241, "lon": -86.158436}, 
                {"lat": 39.7622292, "lon": -86.1578917}]


def euclidean(l1, l2):
    return ((l1[0]**2)-(l2[0]**2)) + ((l1[1]**2)-(l2[1]**2)) 

pairs = [j for j in combinations([i.values() for i in coords], 2)]
pairs.sort(key= lambda x: euclidean(*x))
print pairs[-1]
