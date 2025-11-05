df = pd.DataFrame({'A': [2, 1, np.nan, 6], 'B': [4, np.nan, 8, np.nan]})

a = df.to_numpy()
print(a)
# [[ 2.  4.]
#  [ 1. nan]
#  [nan  8.]
#  [ 6. nan]]

a = np.where(np.isnan(a), np.nanmean(a, axis=0), a) 
print(a)   
