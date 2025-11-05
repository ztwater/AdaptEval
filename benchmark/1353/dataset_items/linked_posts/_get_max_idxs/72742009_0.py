maxvals = np.amax(windows, axis=(2, 3))
# array([[92, 92, 87, 87],
#        [86, 86, 87, 87],
#        [75, 75, 83, 87]])

indx = np.array((windows == np.expand_dims(maxvals, axis = (2, 3)).nonzero())
