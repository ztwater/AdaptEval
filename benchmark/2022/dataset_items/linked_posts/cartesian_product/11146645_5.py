In [5]: test_cartesian(*(x100 * 3))
cartesian_product:
8.8 ms ± 138 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product_transpose:
7.87 ms ± 91.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product_itertools:
518 ms ± 5.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [6]: test_cartesian(*(x50 * 4))
cartesian_product:
169 ms ± 5.1 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
cartesian_product_transpose:
184 ms ± 4.32 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
cartesian_product_itertools:
3.69 s ± 73.5 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [7]: test_cartesian(*(x10 * 6))
cartesian_product:
26.5 ms ± 449 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)
cartesian_product_transpose:
16 ms ± 133 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product_itertools:
728 ms ± 16 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

In [8]: test_cartesian(*(x10 * 7))
cartesian_product:
650 ms ± 8.14 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
cartesian_product_transpose:
518 ms ± 7.09 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
cartesian_product_itertools:
8.13 s ± 122 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
