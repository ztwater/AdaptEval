%%timeit
np.array(index_slice)[np.where(df.loc[index_slice]['column_name'] >= threshold)[0]]
# 600 µs ± 1.21 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)

%%timeit
[i for i in index_slice if i in df.index[df['column_name'] >= threshold].tolist()]
# 22.5 ms ± 29.1 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
