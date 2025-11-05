>>> a = [1, 2, 3, 4, 5, 6]
>>> z = [(a[x], a[x+1]) for x in range(0, len(a)-1)]
>>> z
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
# Replacing it with the test
>>> z = [(a[x] == a[x+1]) for x in range(0, len(a)-1)]
>>> z
[False, False, False, False, False]
>>> if False in z : Print "All elements are not equal"
