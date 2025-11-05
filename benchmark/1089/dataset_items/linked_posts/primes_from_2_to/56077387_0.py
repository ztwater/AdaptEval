import numpy as np 
def generate_primes(n):
    is_prime = np.ones(n+1,dtype=bool)
    is_prime[0:2] = False
    for i in range(int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i**2::i]=False
    return np.where(is_prime)[0]
