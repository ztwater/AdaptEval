from scipy.spatial.transform import Rotation as R
import numpy as np

def get_rotation_matrix(vec2, vec1=np.array([1, 0, 0])):
    """get rotation matrix between two vectors using scipy"""
    vec1 = np.reshape(vec1, (1, -1))
    vec2 = np.reshape(vec2, (1, -1))
    r = R.align_vectors(vec2, vec1)
    return r[0].as_matrix()


vec1 = np.array([2, 3, 2.5])
vec2 = np.array([-3, 1, -3.4])

mat = get_rotation_matrix(vec1=vec1, vec2=vec2)
print(mat)
vec1_rot = mat.dot(vec1)
assert np.allclose(vec1_rot / np.linalg.norm(vec1_rot), vec2 / np.linalg.norm(vec2))
