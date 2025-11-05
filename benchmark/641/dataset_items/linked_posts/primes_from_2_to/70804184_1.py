In[10]:
%timeit nb_primes(1_000_000)

Out[10]:
2.47 ms ± 36.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

In[11]:
%timeit nb_primes(10_000_000)

Out[11]:
33.4 ms ± 373 µs per loop (mean ± std. dev. of 7 runs, 10 loops each)

In[12]:
%timeit nb_primes(100_000_000)

Out[12]:
828 ms ± 5.64 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
