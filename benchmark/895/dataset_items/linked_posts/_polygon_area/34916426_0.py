import math

def area_polygon(n, s):
    return 0.25 * n * s**2 / math.tan(math.pi/n)
