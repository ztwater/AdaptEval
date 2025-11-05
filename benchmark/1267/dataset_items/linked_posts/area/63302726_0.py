from shapely.geometry import Polygon
import numpy as np
def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))
coords = np.random.rand(6, 2)
x, y = coords[:, 0], coords[:, 1]
