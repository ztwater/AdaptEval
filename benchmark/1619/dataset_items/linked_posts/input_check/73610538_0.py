from matplotlib import pyplot as plt

# Some other code you've written
...

# Your data generation goes here
xdata = ...
ydata = ...
colordata = function(xdata, ydata)

# Your plotting stuff begins here
fig, ax = plt.subplots(1)
im = ax.scatterplot(xdata, ydata, c=colordata)

# Create a new axis which will be the parent for the colour bar
# Note that this solution is independent of the 'fig' object
ax2 = ax.twinx()
ax2.tick_params(which="both", right=False, labelright=False)

# Add the colour bar itself
plt.colorbar(im, ax=ax2)

# More of your code
...

plt.show()
