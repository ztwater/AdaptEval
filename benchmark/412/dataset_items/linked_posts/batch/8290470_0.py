>>> def batch(iterable, n = 1):
...    current_batch = []
...    for item in iterable:
...        current_batch.append(item)
...        if len(current_batch) == n:
...            yield current_batch
...            current_batch = []
...    if current_batch:
...        yield current_batch
...
>>> for x in batch(range(0, 10), 3):
...     print x
...
[0, 1, 2]
[3, 4, 5]
[6, 7, 8]
[9]
