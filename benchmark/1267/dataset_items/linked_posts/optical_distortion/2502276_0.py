def dist(x,y):
    return sqrt(x*x+y*y)

def correct_fisheye(src_size,dest_size,dx,dy,factor):
    """ returns a tuple of source coordinates (sx,sy)
        (note: values can be out of range)"""
    # convert dx,dy to relative coordinates
    rx, ry = dx-(dest_size[0]/2), dy-(dest_size[1]/2)
    # calc theta
    r = dist(rx,ry)/(dist(src_size[0],src_size[1])/factor)
    if 0==r:
        theta = 1.0
    else:
        theta = atan(r)/r
    # back to absolute coordinates
    sx, sy = (src_size[0]/2)+theta*rx, (src_size[1]/2)+theta*ry
    # done
    return (int(round(sx)),int(round(sy)))
