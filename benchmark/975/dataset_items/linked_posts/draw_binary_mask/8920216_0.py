import numpy as np
import matplotlib.pylab as plt

x=np.arange(-3,3.5,.5)
y1=-x**2+9
y2=-x**2+10
plt.fill_between(x,y1,y2)
