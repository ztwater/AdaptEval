import math3d as m3d
r = m3d.Orientation.new_axis_angle([1,2,3], 1)
v = m3d.Vector(4,5,6)
print(r * v)
