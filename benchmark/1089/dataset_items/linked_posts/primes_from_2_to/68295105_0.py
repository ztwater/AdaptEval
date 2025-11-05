import numpy as np
from bitarray import bitarray


def bit_primes(n):
    bit_sieve = bitarray(n // 3 + (n % 6 == 2))
    bit_sieve.setall(1)
    bit_sieve[0] = False

    for i in range(int(n ** 0.5) // 3 + 1):
        if bit_sieve[i]:
            k = 3 * i + 1 | 1
            bit_sieve[k * k // 3::2 * k] = False
            bit_sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = False

    np_sieve = np.unpackbits(np.frombuffer(bit_sieve.tobytes(), dtype=np.uint8)).view(bool)
    return np.concatenate(((2, 3), ((3 * np.flatnonzero(np_sieve) + 1) | 1)))
