import numpy as np
from numba import njit

@njit
def nb_primes(n):
    # Generates prime numbers 2 <= p <= n
    # Atkin's sieve -- see https://en.wikipedia.org/w/index.php?title=Prime_number&oldid=111775466
    sqrt_n = int(np.sqrt(n)) + 1

    # initialize the sieve
    s = np.full(n + 1, -1, dtype=np.int8)
    s[2] = 1
    s[3] = 1

    # put in candidate primes:
    # integers which have an odd number of
    # representations by certain quadratic forms
    for x in range(1, sqrt_n):
        x2 = x * x
        for y in range(1, sqrt_n):
            y2 = y * y
            k = 4 * x2 + y2
            if k <= n and (k % 12 == 1 or k % 12 == 5): s[k] *= -1
            k = 3 * x2 + y2
            if k <= n and (k % 12 == 7): s[k] *= -1
            k = 3 * x2 - y2
            if k <= n and x > y and k % 12 == 11: s[k] *= -1

    # eliminate composites by sieving
    for k in range(5, sqrt_n):
        if s[k]:
            k2 = k*k
            # k is prime, omit multiples of its square; this is sufficient because
            # composites which managed to get on the list cannot be square-free
            for i in range(1, n // k2 + 1):
                j = i * k2 # j ∈ {k², 2k², 3k², ..., n}
                s[j] = -1
    return np.nonzero(s>0)[0]

# initial run for "compilation" 
nb_primes(10)
