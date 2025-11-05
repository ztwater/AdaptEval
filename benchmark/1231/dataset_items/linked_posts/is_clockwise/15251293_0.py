def segments(poly):
    """A sequence of (x,y) numeric coordinates pairs """
    return zip(poly, poly[1:] + [poly[0]])

def check_clockwise(poly):
    clockwise = False
    if (sum(x0*y1 - x1*y0 for ((x0, y0), (x1, y1)) in segments(poly))) < 0:
        clockwise = not clockwise
    return clockwise

poly = [(2,2),(6,2),(6,6),(2,6)]
check_clockwise(poly)
False

poly = [(2, 6), (6, 6), (6, 2), (2, 2)]
check_clockwise(poly)
True
