import shapely.plotting
from shapely.geometry import Polygon

polygon1 = Polygon([(0, 5), (1, 1), (3, 0)])

shapely.plotting.plot_polygon(polygon1)
