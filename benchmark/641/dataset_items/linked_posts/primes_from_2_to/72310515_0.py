import numexpr as ne
import numpy as np

def primesfrom2to_numexpr(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=24, Returns a array of primes, 2 <= p < n + a few over"""
    sieve = np.zeros((n // 3 + (n % 6 == 2))//4+1, dtype=np.int32)
    ne.evaluate('sieve + 0x01010101', out=sieve)
    sieve = sieve.view('int8')
    #sieve = np.ones(n // 3 + (n % 6 == 2), dtype=np.bool_)
    sieve[0] = 0
    for i in np.arange(int(n ** 0.5) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[((k * k) // 3)::2 * k] = 0
            sieve[(k * k + 4 * k - 2 * k * (i & 1)) // 3::2 * k] = 0
    sieve[[0,8]] = 1
    result = np.flatnonzero(sieve)
    ne.evaluate('result * 3 + 1 + result%2', out=result)
    result[:9] = [2,3,5,7,11,13,17,19,23]
    return result
