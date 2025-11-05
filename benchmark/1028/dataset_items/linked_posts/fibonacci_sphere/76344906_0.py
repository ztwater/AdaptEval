import math
def spherical_coordinate(x, y):
    return [
        math.cos(x) * math.cos(y),
        math.sin(x) * math.cos(y),
        math.sin(y)
    ]

def NX(n, x):
    pts = []
    start = (-1. + 1. / (n - 1.))
    increment = (2. - 2. / (n - 1.)) / (n - 1.)
    for j in xrange(0, n):
        s = start + j * increment
        pts.append(
            spherical_cordinate(
                s * x, math.pi / 2. *
                math.copysign(1, s) *
                (1. - math.sqrt(1. - abs(s)))
            )
        )
    return pts

def generate_points(n):
    return NX(n, 0.1 + 1.2 * n)
