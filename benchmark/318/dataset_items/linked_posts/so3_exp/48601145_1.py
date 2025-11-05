import numpy as np
np.set_printoptions(suppress=True)

from mgen import rotation_around_axis
from mgen import rotation_from_angles
from mgen import rotation_around_x

matrix = rotation_from_angles([np.pi/2, 0, 0], 'XYX')
matrix.dot([0, 1, 0])
# array([0., 0., 1.])

matrix = rotation_around_axis([1, 0, 0], np.pi/2)
matrix.dot([0, 1, 0])
# array([0., 0., 1.])

matrix = rotation_around_x(np.pi/2)
matrix.dot([0, 1, 0])
# array([0., 0., 1.])
