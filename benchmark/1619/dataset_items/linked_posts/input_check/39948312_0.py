projection = cartopy.crs.UTM(zone='17N')
ax = plt.axes(projection=projection)
im = ax.imshow(np.arange(200).reshape((20, 10)))
