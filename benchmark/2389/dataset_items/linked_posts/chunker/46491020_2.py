from iteration_utilities import grouper
seq = list(range(17))
for group in grouper(seq, 4):
    print(group)
# (0, 1, 2, 3)
# (4, 5, 6, 7)
# (8, 9, 10, 11)
# (12, 13, 14, 15)
# (16,)

for group in grouper(seq, 4, fillvalue=None):
    print(group)
# (0, 1, 2, 3)
# (4, 5, 6, 7)
# (8, 9, 10, 11)
# (12, 13, 14, 15)
# (16, None, None, None)

for group in grouper(seq, 4, truncate=True):
    print(group)
# (0, 1, 2, 3)
# (4, 5, 6, 7)
# (8, 9, 10, 11)
# (12, 13, 14, 15)
