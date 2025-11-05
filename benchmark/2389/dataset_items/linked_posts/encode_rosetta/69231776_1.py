mean = np.nanmean(m, axis=0)
idx = np.where(np.isnan(m))
m[idx] = np.take(mean, idx[1])
print(m)

# Output
array([[1., 5.],
       [3., 5.],
       [2., 8.],
       [6., 2.]])
