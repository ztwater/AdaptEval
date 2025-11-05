from iteration_utilities import grouper
seq = list(range(20))
for group in grouper(seq, 4):
    print(group)
