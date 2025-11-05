>>> timeit.timeit('primes.rwh_primes2(10**8)', setup='import primes', number=1)
6.394284538007014
>>> timeit.timeit('primes.rwh_primes2_python3(10**8)', setup='import primes', number=1)
3.833829450302801
