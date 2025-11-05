from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm

u = array([1.,2,3,4])
v = ...
c = dot(u,v)/norm(u)/norm(v) # -> cosine of the angle
angle = arccos(clip(c, -1, 1)) # if you really want the angle
