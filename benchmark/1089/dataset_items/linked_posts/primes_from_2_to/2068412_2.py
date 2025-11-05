$ python2.5 -mtimeit -s'import pri' 'pri.get_primes(1000000)'
10 loops, best of 3: 1.69 sec per loop
$ python2.5 -mtimeit -s'import pri' 'pri.get_primes_erat(1000000)'
10 loops, best of 3: 673 msec per loop
