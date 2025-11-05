from time import clock
import platform

def benchmark(iterations, limit):
    start = clock()
    for x in range(iterations):
        half_sieve(limit)
    end = clock() - start
    print(f'{end/iterations:.4f} seconds for primes < {limit}')

if __name__ == '__main__':
    print(platform.python_version())
    print(platform.platform())
    print(platform.processor())
    it = 10
    for pw in range(4, 9):
        benchmark(it, 10**pw)
