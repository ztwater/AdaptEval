%timeit -r10 -n1000 pd.to_datetime(dates).year.tolist()
# 304 µs ± 32.2 µs per loop (mean ± std. dev. of 10 runs, 1000 loops each)
