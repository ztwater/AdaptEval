from shapely.geometry import Polygon
import matplotlib.pyplot as plt


# Input polygon with two holes
# (remember exterior point order is ccw, holes cw else
# holes may not appear as holes.)
polygon = Polygon(shell=((0,0),(10,0),(10,10),(0,10)),
                  holes=(((1,3),(5,3),(5,1),(1,1)),
                         ((9,9),(9,8),(8,8),(8,9))))

fig, ax = plt.subplots()
plot_polygon(ax, polygon, facecolor='lightblue', edgecolor='red')
