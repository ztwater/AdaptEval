$ python -mtimeit -s'import sieve' 'sieve.sieve(1000000)' 
10 loops, best of 3: 445 msec per loop
$ cat sieve.py
from math import sqrt

def sieve(size):
 prime=[True]*size
 rng=xrange
 limit=int(sqrt(size))

 for i in rng(3,limit+1,+2):
  if prime[i]:
   prime[i*i::+i]=[False]*len(prime[i*i::+i])

 return [2]+[i for i in rng(3,size,+2) if prime[i]]

if __name__=='__main__':
 print sieve(100)
