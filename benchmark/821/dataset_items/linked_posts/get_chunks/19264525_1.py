from itertools import chain, islice

def chunks(n, iterable):
   iterable = iter(iterable)
   while True:
       yield chain([next(iterable)], islice(iterable, n-1))
