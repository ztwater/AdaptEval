   def dist2line2(x,y,line):
     x1,y1,x2,y2=line
     vx = x1 - x
     vy = y1 - y
     ux = x2-x1
     uy = y2-y1
     length = ux * ux + uy * uy
     det = (-vx * ux) + (-vy * uy) #//if this is < 0 or > length then its outside the line segment
     if det < 0:
       return (x1 - x)**2 + (y1 - y)**2
     if det > length:
       return (x2 - x)**2 + (y2 - y)**2
     det = ux * vy - uy * vx
     return det**2 / length
   def dist2line(x,y,line): return math.sqrt(dist2line2(x,y,line))
