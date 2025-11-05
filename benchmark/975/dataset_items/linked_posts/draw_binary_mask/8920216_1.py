import numpy as np
import matplotlib.pylab as plt

x=np.arange(-3,3.5,.5)
y1=-x**2+9
y2=0
plt.fill_between(x,y1,y2)
circ=plt.Circle((0,4),2,color='w')
ax=plt.gca()
ax.add_patch(circ)
plt.show()
