from numpy import arctan, pi, signbit
from numpy.linalg import norm


def angle_btw(v1, v2):
    u1 = v1 / norm(v1)
    u2 = v2 / norm(v2)

    y = u1 - u2
    x = u1 + u2

    a0 = 2 * arctan(norm(y) / norm(x))

    if (not signbit(a0)) or signbit(pi - a0):
        return a0
    elif signbit(a0):
        return 0.0
    else:
        return pi
