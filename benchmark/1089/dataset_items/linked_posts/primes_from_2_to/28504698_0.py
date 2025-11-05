# You have to list primes upto n
nums = xrange(2, n)
for i in range(2, 10):
    nums = filter(lambda s: s==i or s%i, nums)
print nums
