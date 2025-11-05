In [2]: test_all(*(x100 * 2))
repeat_product:
67.5 µs ± 633 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
dstack_product:
67.7 µs ± 1.09 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
cartesian_product:
33.4 µs ± 558 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
cartesian_product_transpose:
67.7 µs ± 932 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
cartesian_product_recursive:
215 µs ± 6.01 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
cartesian_product_itertools:
3.65 ms ± 38.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In [3]: test_all(*(x500 * 2))
repeat_product:
1.31 ms ± 9.28 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
dstack_product:
1.27 ms ± 7.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
cartesian_product:
375 µs ± 4.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
cartesian_product_transpose:
488 µs ± 8.88 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
cartesian_product_recursive:
2.21 ms ± 38.4 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product_itertools:
105 ms ± 1.17 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)

In [4]: test_all(*(x1000 * 2))
repeat_product:
10.2 ms ± 132 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
dstack_product:
12 ms ± 120 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product:
4.75 ms ± 57.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product_transpose:
7.76 ms ± 52.7 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product_recursive:
13 ms ± 209 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
cartesian_product_itertools:
422 ms ± 7.77 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
