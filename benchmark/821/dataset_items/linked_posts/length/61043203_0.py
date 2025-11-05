import numpy as np

vector1 = [1,0,0]
vector2 = [0,1,0]

unit_vector1 = vector1 / np.linalg.norm(vector1)
unit_vector2 = vector2 / np.linalg.norm(vector2)

dot_product = np.dot(unit_vector1, unit_vector2)

angle = np.arccos(dot_product) #angle in radian
