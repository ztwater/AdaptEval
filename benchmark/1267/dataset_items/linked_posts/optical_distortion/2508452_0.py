
def dist(x,y):
    return sqrt(x*x+y*y)

def fisheye_to_rectilinear(src_size,dest_size,sx,sy,crop_factor,zoom):
    """ returns a tuple of dest coordinates (dx,dy)
        (note: values can be out of range)
 crop_factor is ratio of sphere diameter to diagonal of the source image"""  
    # convert sx,sy to relative coordinates
    rx, ry = sx-(src_size[0]/2), sy-(src_size[1]/2)
    r = dist(rx,ry)

    # focal distance = radius of the sphere
    pi = 3.1415926535
    f = dist(src_size[0],src_size[1])*factor/pi

    # calc theta 1) linear mapping (older Nikon) 
    theta = r / f

    # calc theta 2) nonlinear mapping 
    # theta = asin ( r / ( 2 * f ) ) * 2

    # calc new radius
    nr = tan(theta) * zoom

    # back to absolute coordinates
    dx, dy = (dest_size[0]/2)+rx/r*nr, (dest_size[1]/2)+ry/r*nr
    # done
    return (int(round(dx)),int(round(dy)))


def fisheye_auto_zoom(src_size,dest_size,crop_factor):
    """ calculate zoom such that left edge of source image matches left edge of dest image """
    # Try to see what happens with zoom=1
    dx, dy = fisheye_to_rectilinear(src_size, dest_size, 0, src_size[1]/2, crop_factor, 1)

    # Calculate zoom so the result is what we wanted
    obtained_r = dest_size[0]/2 - dx
    required_r = dest_size[0]/2
    zoom = required_r / obtained_r
    return zoom
