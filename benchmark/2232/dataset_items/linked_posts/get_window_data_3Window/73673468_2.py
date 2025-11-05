n = 20_000_000
df = pd.DataFrame({'NumCol': np.random.rand(n).astype('float16'), 
                   'BoolCol': np.random.default_rng().choice([True, False], size=n)})

%timeit df.index[df['BoolCol']]
# 181 ms ± 2.47 ms per loop (mean ± std. dev. of 10 runs, 1000 loops each)

%timeit df['BoolCol'].pipe(lambda x: x.index[x])
# 181 ms ± 1.08 ms per loop (mean ± std. dev. of 10 runs, 1000 loops each)

%timeit df['BoolCol'].loc[lambda x: x].index
# 297 ms ± 7.15 ms per loop (mean ± std. dev. of 10 runs, 1000 loops each)
