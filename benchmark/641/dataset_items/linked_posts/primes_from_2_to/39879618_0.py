python -m timeit -r10 -s"from sympy import sieve" "primes = list(sieve.primerange(1, 10**6))"
