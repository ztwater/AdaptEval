df = pd.DataFrame({'A': [1, np.nan, 2, 6], 'B': [5, np.nan, 8, 2]})

m = df.to_numpy()
print(m)

# Output
array([[ 1.,  5.],
       [nan, nan],
       [ 2.,  8.],
       [ 6.,  2.]])
