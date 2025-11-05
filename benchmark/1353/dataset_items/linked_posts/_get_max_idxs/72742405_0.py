unique_values, index = np.unique(a, return_index=True)
result = index[np.searchsorted(unique_values, np.amax(windows, axis=(2, 3)))]
ind = np.dstack((result % a.shape[1], result // a.shape[1]))

ind.reshape(12, 2)
# [[1 0]
#  [1 0]
#  [4 1]
#  [5 1]
#  [1 1]
#  [1 1]
#  [4 1]
#  [5 1]
#  [1 4]
#  [1 4]
#  [4 4]
#  [4 4]]
