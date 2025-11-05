import numpy as np
import quaternion as quat

v = [3,5,0]
axis = [4,4,1]
theta = 1.2 #radian

vector = np.array([0.] + v)
rot_axis = np.array([0.] + axis)
axis_angle = (theta*0.5) * rot_axis/np.linalg.norm(rot_axis)
