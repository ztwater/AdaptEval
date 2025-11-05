from shapely.geometry import Polygon
pgon = Polygon(zip(x, y)) # Assuming the OP's x,y coordinates

print(pgon.area)
