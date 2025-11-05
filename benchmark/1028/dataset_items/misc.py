# this is a file to host random assorted scripts that were useful at some place in the code

import numpy as np

def fibonacci_sphere(N):
    """
    Creates N regularly and equidistantly distributed points on the surface of a sphere with radius 1.
    see: https://stackoverflow.com/questions/9600801/evenly-distributing-n-points-on-a-sphere
    """

    points = []
    phi = np.pi * (np.sqrt(5.) - 1.)  # golden angle in radians

    for i in range(N):
        y = 1 - (i / float(N - 1)) * 2  # y goes from 1 to -1
        radius = np.sqrt(1 - y * y)  # radius at y

        theta = phi * i  # golden angle increment

        x = np.cos(theta) * radius
        z = np.sin(theta) * radius

        points.append([x, y, z])
        # points.append((x, y, z))

    return np.array(points)
    # return points

