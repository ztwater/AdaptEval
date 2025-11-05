a = np.arange(1000)
ii = [700,2000,10000] # The indices you want of the tiled array
b = a[np.mod(ii,a.size)]
