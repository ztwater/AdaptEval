from shapely.ops import nearest_points
p2 = nearest_points(line, p)[0]
print(p2)  # POINT (5 7)
