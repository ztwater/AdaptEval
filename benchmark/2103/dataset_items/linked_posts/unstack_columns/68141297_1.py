A, B, = unstack([[1, 2], [3, 4]], axis=1)
assert list(A) == [1, 3]
assert list(B) == [2, 4]
