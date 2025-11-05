import sys

def miller_rabin_pass(a, n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    if n <= 2:
        return n == 2

    if n < 2_047:
        return miller_rabin_pass(2, n)

    return all(miller_rabin_pass(a, n) for a in (31, 73))


n = int(sys.argv[1])
primes = [2]
for p in range(3,n,2):
  if miller_rabin(p):
    primes.append(p)
print len(primes)
