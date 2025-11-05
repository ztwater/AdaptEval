points = (point1, point2, point3, point3D)
xs = [point.x for point in points]
ys = [point.y for point in points]

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.scatter(xs, ys)
