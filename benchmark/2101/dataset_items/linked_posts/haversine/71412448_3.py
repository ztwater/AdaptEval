# Import sin, cos, atan2, and sqrt from the 'math' module
from math import sin, cos, atan2, sqrt

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))
d = r * c
