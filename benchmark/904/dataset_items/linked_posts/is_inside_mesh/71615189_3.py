import matplotlib.pyplot as plt
import numpy as np
x = [-8,-4.19,-3.54,-3.31,-2.56,-2.31,-1.66,-0.96,-0.22,0.62,1.21,3]
y = [-0.01,0.01,0.03,0.04,0.07,0.09,0.16,0.28,0.45,0.65,0.77,1]
x = np.asfarray(x)
y = np.asfarray(y)

plt.scatter(x, y)
x_new= np.linspace(min(x), max(x), 10000)
y_new = cubic_interpolate(x_new, x, y)
plt.plot(x_new, y_new)

from scipy.interpolate import CubicSpline
f = CubicSpline(x, y, bc_type='natural')
plt.plot(x_new, f(x_new), label='ref')
plt.legend()
plt.show()
