from math import sqrt
from time import *
prime_list = [2]
n = int(input())
s = time()
for n0 in range(2,n+1):
    for i0 in prime_list:
        if n0%i0==0:
            break
        elif i0>=int(sqrt(n0)):
            prime_list.append(n0)
            break
e = time()
print(e-s)
#print(prime_list); print(f'pi({n})={len(prime_list)}')
print(f'{n}: {len(prime_list)}, time: {e-s}')
