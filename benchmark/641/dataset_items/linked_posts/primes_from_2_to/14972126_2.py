#!/usr/bin/env python
import time

def GetPrimes3(n):

    Sieve = [1 for x in xrange(n)]

    for q in xrange (3, n, 2):
        k = q
        for y in xrange(k*k, n, k << 1):
            Sieve[y] = 0

    return Sieve



start = time.clock()

d = 10000000
Primes = GetPrimes3(d)

count = 1 #This is for 2

for x in xrange (3, d, 2):
    if Primes[x]:
        count+=1

elapsed = (time.clock() - start)
print "\nFound", count, "primes in", elapsed, "seconds!\n"
