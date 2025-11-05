def find_primes(n):
    # Create a boolean list to track prime numbers
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    # Mark all multiples of 2 as composite (except 2 itself)
    for i in range(4, n+1, 2):
        primes[i] = False

    # Iterate over all odd numbers and mark their multiples as composite
    for i in range(3, int(n**0.5)+1, 2):
        if primes[i]:
            for j in range(i*i, n+1, 2*i):
                primes[j] = False

    # Return a list of prime numbers
    return [i for i in range(n+1) if primes[I]]
primes = find_primes(1000000)
print(primes)
