it = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
for chunk in zip(it, it, it, it):
    print chunk

>>> (1, 2, 3, 4)
>>> (5, 6, 7, 8)
