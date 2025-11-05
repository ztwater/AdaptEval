#!/usr/bin/env python
import time

def GetPrimes(n):

    Sieve = [1 for x in xrange(n)]

    Done = False
    w = 3

    while not Done:

        for q in xrange (3, n, 2):
            Prod = w*q
            if Prod < n:
                Sieve[Prod] = 0
            else:
                break

        if w > (n/2):
            Done = True
        w += 2

    return Sieve



start = time.clock()

d = 10000000
Primes = GetPrimes(d)

count = 1 #This is for 2

for x in xrange (3, d, 2):
    if Primes[x]:
        count+=1

elapsed = (time.clock() - start)
print "\nFound", count, "primes in", elapsed, "seconds!\n"
