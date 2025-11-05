dy = p1.y - p2.y
dX = p2.x - p1.x

rads = atan2(dy,dx)
degs = degrees(rads)
if degs < 0 :
   degs +=90
