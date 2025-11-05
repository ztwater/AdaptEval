import numpy as np
import matplotlib.pyplot as plt





r= 30.*np.sqrt(np.random.rand(1000))
#r= 30.*np.random.rand(1000)
phi = 2. * np.pi * np.random.rand(1000)



x = r * np.cos(phi)
y = r * np.sin(phi)


plt.figure()
plt.plot(x,y,'.')
plt.show()