from math import radians, sin, cos

def rotate_point_wrt_center(point_to_be_rotated, angle, center_point = (0,0)):
        
    angle = radians(angle)
        
    xnew = cos(angle)*(point_to_be_rotated[0] - center_point[0]) - sin(angle)*(point_to_be_rotated[1] - center_point[1]) + center_point[0]
    ynew = sin(angle)*(point_to_be_rotated[0] - center_point[0]) + cos(angle)*(point_to_be_rotated[1] - center_point[1]) + center_point[1]
    
    return (round(xnew,2),round(ynew,2))
