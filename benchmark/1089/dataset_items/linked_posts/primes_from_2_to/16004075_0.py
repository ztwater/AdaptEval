from bitarray import bitarray
def primes_to(n):
    size = n//2
    sieve = bitarray(size)
    sieve.setall(1)
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            sieve[(i+i*val)::val] = 0
    return [2] + [2*i+1 for i, v in enumerate(sieve) if v and i > 0]

python -m timeit -n10 -s "import euler" "euler.primes_to(1000000000)"
10 loops, best of 3: 46.5 sec per loop
