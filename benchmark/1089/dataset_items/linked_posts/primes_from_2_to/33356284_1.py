>>> timeit.timeit('primes.rwh_primes2(10**6)', setup='import primes', number=1)
0.0652179726976101
>>> timeit.timeit('primes.rwh_primes2_python3(10**6)', setup='import primes', number=1)
0.03267321276325674
