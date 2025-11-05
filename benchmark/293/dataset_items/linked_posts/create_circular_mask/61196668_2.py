x = np.linspace(-10, 10, 491)
y = np.linspace(-10, 10, 491)
x, y = np.meshgrid(x, y)
x_0 = -3
y_0 = -6
mask = np.sqrt((x-x_0)**2+(y-y_0)**2)
