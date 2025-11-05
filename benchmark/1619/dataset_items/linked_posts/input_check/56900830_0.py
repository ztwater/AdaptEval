import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax = plt.axes()
im = ax.imshow(np.arange(100).reshape((10,10)))

# Create an axes for colorbar. The position of the axes is calculated based on the position of ax.
# You can change 0.01 to adjust the distance between the main image and the colorbar.
# You can change 0.02 to adjust the width of the colorbar.
# This practice is universal for both subplots and GeoAxes.

cax = fig.add_axes([ax.get_position().x1+0.01,ax.get_position().y0,0.02,ax.get_position().height])
plt.colorbar(im, cax=cax) # Similar to fig.colorbar(im, cax = cax)
