from scipy.spatial.transform import Rotation
from numpy.linalg import norm


v = [3, 5, 0]
axis = [4, 4, 1]
theta = 1.2

axis = axis / norm(axis)  # normalize the rotation vector first
rot = Rotation.from_rotvec(theta * axis)

new_v = rot.apply(v)  
print(new_v)    # results in [2.74911638 4.77180932 1.91629719]
