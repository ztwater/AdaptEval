    # Program to calculate Primes
 primes = [1,3,5,7]
for n in range(9,100000,2):
    for x in range(1,(len(primes)/2)):
        if n % primes[x] == 0:
            break
    else:
        primes.append(n)
print primes
