import numpy as np
import shapely.geometry as sg
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def add_polygon_patch(coords, ax, fc='blue'):
    patch = patches.Polygon(np.array(coords.xy).T, fc=fc)
    ax.add_patch(patch)


border = [(-10, -10), (-10, 10), (10, 10), (10, -10)]  # Large square
holes = [
    [(-6, -2), (-6, 2), (-2, 2), (-2, -2)],  # Square hole
    [(2, -2), (4, 2), (6, -2)]               # Triangle hole
]
region = sg.Polygon(shell=border, holes=holes)

fig, ax = plt.subplots(1, 1)

add_polygon_patch(region.exterior, ax)
for interior in region.interiors:
    add_polygon_patch(interior, ax, 'white')
        
ax.axis('equal')
plt.show()
