  from pyquaternion import Quaternion
  v = [3,5,0]
  axis = [4,4,1]
  theta = 1.2 #radian
  rotated_v = Quaternion(axis=axis,angle=theta).rotate(v)
