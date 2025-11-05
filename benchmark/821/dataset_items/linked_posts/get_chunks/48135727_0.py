import time
batch_size = 7
arr_len = 298937

#---------slice-------------

print("\r\nslice")
start = time.time()
arr = [i for i in range(0, arr_len)]
while True:
    if not arr:
        break

    tmp = arr[0:batch_size]
    arr = arr[batch_size:-1]
print(time.time() - start)

#-----------index-----------

print("\r\nindex")
arr = [i for i in range(0, arr_len)]
start = time.time()
for i in range(0, round(len(arr) / batch_size + 1)):
    tmp = arr[batch_size * i : batch_size * (i + 1)]
print(time.time() - start)

#----------batches 1------------

def batch(iterable, n=1):
    l = len(iterable)
    for ndx in range(0, l, n):
        yield iterable[ndx:min(ndx + n, l)]

print("\r\nbatches 1")
arr = [i for i in range(0, arr_len)]
start = time.time()
for x in batch(arr, batch_size):
    tmp = x
print(time.time() - start)

#----------batches 2------------

from itertools import islice, chain

def batch(iterable, size):
    sourceiter = iter(iterable)
    while True:
        batchiter = islice(sourceiter, size)
        yield chain([next(batchiter)], batchiter)


print("\r\nbatches 2")
arr = [i for i in range(0, arr_len)]
start = time.time()
for x in batch(arr, batch_size):
    tmp = x
print(time.time() - start)

#---------chunks-------------
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
print("\r\nchunks")
arr = [i for i in range(0, arr_len)]
start = time.time()
for x in chunks(arr, batch_size):
    tmp = x
print(time.time() - start)

#-----------grouper-----------

from itertools import zip_longest # for Python 3.x
#from six.moves import zip_longest # for both (uses the six compat library)

def grouper(iterable, n, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

arr = [i for i in range(0, arr_len)]
print("\r\ngrouper")
start = time.time()
for x in grouper(arr, batch_size):
    tmp = x
print(time.time() - start)
