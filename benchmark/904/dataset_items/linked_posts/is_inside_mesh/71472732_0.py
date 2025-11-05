from scipy.interpolate import CubicSpline
import numpy as np

x = [-5,-4.19,-3.54,-3.31,-2.56,-2.31,-1.66,-0.96,-0.22,0.62,1.21,3]
y = [-0.01,0.01,0.03,0.04,0.07,0.09,0.16,0.28,0.45,0.65,0.77,1]
value = 2

#ascending order
if np.any(np.diff(x) < 0):
    indexes = np.argsort(x).astype(int)
    x = np.array(x)[indexes]
    y = np.array(y)[indexes]

f = CubicSpline(x, y, bc_type='natural')
specificVal = f(value).item(0) #f(value) is numpy.ndarray!!
print(specificVal)
