import numpy as np
from shapely.geometry import Polygon

points = np.array([
    (5,0),
    (6,4),
    (4,5),
    (1,5),
    (1,0)
])

P = Polygon(points)
