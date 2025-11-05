fig, ax = plt.subplots(2,1,figsize=(12,8)) # Caution, figsize will also influence positions.
im1 = ax[0].imshow(np.arange(100).reshape((10,10)), vmin = -100, vmax =100)
im2 = ax[1].imshow(np.arange(-100,0).reshape((10,10)), vmin = -100, vmax =100)
fig.colorbar(im1, ax=ax)
