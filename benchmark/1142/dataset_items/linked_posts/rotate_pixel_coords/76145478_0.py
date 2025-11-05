import math
def rotate_points(*points,angle=0,center=(0,0)):
    '''
    Rotate one or more 2D points counterclockwise by a given angle (in degrees) around a given center.
    '''
    cx,cy = center
    angle = angle % 360
    ang_rad = math.radians(angle)
    cos_ang,sin_ang = (0,1) if angle==90 else (-1,0) if angle==180 else (0,-1) if angle==270 else (math.cos(ang_rad),math.sin(ang_rad))
    ret = tuple((cx+cos_ang*dx-sin_ang*dy,cy+sin_ang*dx+cos_ang*dy) for dx,dy in ((x-cx,y-cy) for x,y in points))
    return ret if len(ret)>1 else ret[0] # a single point is returned as such and a sequence of points as a tuple
