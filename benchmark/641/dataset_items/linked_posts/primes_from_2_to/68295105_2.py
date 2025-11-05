python3 -m timeit -s "import fast_primes" "fast_primes.bit_primes(500_000_000)"
1 loop, best of 5: 540 msec per loop

python3 -m timeit -s "import fast_primes" "fast_primes.primesfrom2to(500_000_000)"
1 loop, best of 5: 1.15 sec per loop
