from typing import List

def list_primes(limit: int) -> List[int]:
    primes = set(range(2, limit + 1))
    for i in range(2, limit + 1):
        if i in primes:
            primes.difference_update(set(list(range(i, limit + 1, i))[1:]))
    return sorted(primes)

>>> list_primes(100)
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
