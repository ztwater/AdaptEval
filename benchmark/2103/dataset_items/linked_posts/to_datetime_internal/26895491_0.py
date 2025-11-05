dates = np.arange(np.datetime64('2000-01-01'), np.datetime64('2010-01-01'))
years = dates.astype('datetime64[Y]').astype(int) + 1970
months = dates.astype('datetime64[M]').astype(int) % 12 + 1
days = dates - dates.astype('datetime64[M]') + 1
