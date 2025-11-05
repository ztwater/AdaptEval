def get_primes_erat(n):
  return list(itertools.takewhile(lambda p: p<n, erat2()))
