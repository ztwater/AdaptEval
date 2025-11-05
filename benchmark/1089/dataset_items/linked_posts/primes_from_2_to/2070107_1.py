>>>mine = timeit.Timer("daniel_sieve_2(1000000)",
...                    "from sieves import daniel_sieve_2")
>>>prev = timeit.Timer("get_primes_erat(1000000)",
...                    "from sieves import get_primes_erat")
>>>print "Mine: {0:0.4f} ms".format(min(mine.repeat(3, 1))*1000)
Mine: 428.9446 ms
>>>print "Previous Best {0:0.4f} ms".format(min(prev.repeat(3, 1))*1000)
Previous Best 621.3581 ms
