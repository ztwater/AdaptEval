python3 -m timeit -s "import fast_primes" "fast_primes.bit_primes(1000000)"
200 loops, best of 5: 1.19 msec per loop

python3 -m timeit -s "import fast_primes" "fast_primes.primesfrom2to(1000000)"
200 loops, best of 5: 1.23 msec per loop
