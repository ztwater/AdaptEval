from time import time
# 175 ms for all the primes up to the value 10**6
def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    #a[2] = True
    for n in xrange(4, limit, 2):
        a[n] = False
    root_limit = int(limit**.5)+1
    for i in xrange(3,root_limit):
        if a[i]:
            for n in xrange(i*i, limit, 2*i):
                a[n] = False
    return a

LIMIT = 10**6
s=time()
primes = primes_sieve(LIMIT)
print time()-s
