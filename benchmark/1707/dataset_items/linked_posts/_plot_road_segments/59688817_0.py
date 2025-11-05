import geopandas as gpd
import matplotlib.pyplot as plt

shapefile = gpd.read_file("path/to/shapes.shp")
shapefile.plot()
plt.show()

