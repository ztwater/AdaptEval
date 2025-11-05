from shapely.geometry import LineString
import numpy as np

ninety_degrees_rad = 90.0 * np.pi / 180.0

def angle_between(line1, line2):
    coords_1 = line1.coords
    coords_2 = line2.coords

    line1_vertical = (coords_1[1][0] - coords_1[0][0]) == 0.0
    line2_vertical = (coords_2[1][0] - coords_2[0][0]) == 0.0

    # Vertical lines have undefined slope, but we know their angle in rads is = 90° * π/180
    if line1_vertical and line2_vertical:
        # Perpendicular vertical lines
        return 0.0
    if line1_vertical or line2_vertical:
        # 90° - angle of non-vertical line
        non_vertical_line = line2 if line1_vertical else line1
        return abs((90.0 * np.pi / 180.0) - np.arctan(slope(non_vertical_line)))

    m1 = slope(line1)
    m2 = slope(line2)

    return np.arctan((m1 - m2)/(1 + m1*m2))

def slope(line):
    # Assignments made purely for readability. One could opt to just one-line return them
    x0 = line.coords[0][0]
    y0 = line.coords[0][1]
    x1 = line.coords[1][0]
    y1 = line.coords[1][1]
    return (y1 - y0) / (x1 - x0)
