import numpy as np

def unit_vector(var_0):
    """ Returns the unit vector of the vector.  """
    return var_0 / np.linalg.norm(var_0)

def angle_between(var_1, var_2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    var_3 = unit_vector(var_1)
    var_4 = unit_vector(var_2)
    return np.arccos(np.clip(np.dot(var_3, var_4), -1.0, 1.0))
