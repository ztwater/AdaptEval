%timeit -r10 -n1000 [from_numpy_datetime_extract(x, "year") for x in dates]
# 14.3 µs ± 4.03 µs per loop (mean ± std. dev. of 10 runs, 1000 loops each)
