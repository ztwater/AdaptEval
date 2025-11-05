C:\USERS>python -m timeit -n10 -s "import get_primes" "get_primes.get_primes_erat(1000000)"
10 loops, best of 3: 710 msec per loop

C:\USERS>python -m timeit -n10 -s "import get_primes" "get_primes.daniel_sieve_2(1000000)"
10 loops, best of 3: 435 msec per loop

C:\USERS>python -m timeit -n10 -s "import get_primes" "get_primes.sundaram3(1000000)"
10 loops, best of 3: 327 msec per loop
