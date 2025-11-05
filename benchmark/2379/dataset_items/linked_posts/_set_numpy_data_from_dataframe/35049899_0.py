# create an empty array of NaN of the right dimensions
shape = map(len, frame.index.levels)
arr = np.full(shape, np.nan)

# fill it using Numpy's advanced indexing
arr[frame.index.codes] = frame.values.flat
# ...or in Pandas < 0.24.0, use
# arr[frame.index.labels] = frame.values.flat
