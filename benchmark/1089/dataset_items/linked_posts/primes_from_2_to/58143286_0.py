primes = []
for n in range(low, high + 1):
    if all(n % i for i in primes):
        primes.append(n)
