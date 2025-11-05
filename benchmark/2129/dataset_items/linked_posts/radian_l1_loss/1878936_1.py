PI = math.pi
TAU = 2*PI
def smallestSignedAngleBetween(x, y):
    a = (x - y) % TAU
    b = (y - x) % TAU
    return -a if a < b else b
