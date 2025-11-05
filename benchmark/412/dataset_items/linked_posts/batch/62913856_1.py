def my_gen():
    yield from range(10)
 
for batch in batcher(my_gen(), 3):
    print(batch)

>>> [0, 1, 2]
>>> [3, 4, 5]
>>> [6, 7, 8]
>>> [9]

