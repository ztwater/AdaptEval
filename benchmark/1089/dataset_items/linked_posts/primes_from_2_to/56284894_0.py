from itertools import compress

def half_sieve(n):
    """
    Returns a list of prime numbers less than `n`.
    """
    if n <= 2:
        return []
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    primes = list(compress(range(1, n, 2), sieve))
    primes[0] = 2
    return primes
