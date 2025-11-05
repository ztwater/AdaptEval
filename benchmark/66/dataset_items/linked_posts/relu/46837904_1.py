import numpy as np
x = np.random.random((5000, 5000)) - 0.5
print("max method:")
%timeit -n10 np.maximum(x, 0)
print("max inplace method:")
%timeit -n10 np.maximum(x, 0,x)
print("multiplication method:")
%timeit -n10 x * (x > 0)
print("abs method:")
%timeit -n10 (abs(x) + x) / 2
print("fancy index:")
%timeit -n10 x[x<0] =0

max method:
241 ms ± 3.53 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
max inplace method:
38.5 ms ± 4 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
multiplication method:
162 ms ± 3.1 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
abs method:
181 ms ± 4.18 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
fancy index:
20.3 ms ± 272 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
