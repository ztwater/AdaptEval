import matplotlib.pyplot as plt

x,y = P.exterior.coords.xy
plt.plot(x,y)
plt.axis('equal')
plt.grid()
plt.show()
