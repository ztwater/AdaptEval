import math  

def distance_from_segment(x1, y1, x2, y2, x3, y3): # x3, y3 is the point
    # https://stackoverflow.com/questions/10983872/distance-from-a-point-to-a-polygon
    # https://stackoverflow.com/questions/849211/shortest-distance-between-a-point-and-a-line-segment
    px = x2 - x1
    py = y2 - y1
    norm = px*px + py*py
    u = ((x3 - x1) * px + (y3 - y1) * py) / float(norm)
    if u > 1:
        u = 1
    elif u < 0:
        u = 0
    x = x1 + u * px
    y = y1 + u * py
    dx = x - x3
    dy = y - y3
    return math.sqrt(dx*dx + dy*dy)
 
