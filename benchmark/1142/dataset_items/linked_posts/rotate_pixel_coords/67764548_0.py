import numpy as np

def rotate(points, origin, angle):
    return (points - origin) * np.exp(complex(0, angle)) + origin
