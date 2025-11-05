def f(x,y):
  import math
  return min(y-x, y-x+2*math.pi, y-x-2*math.pi, key=abs)
