ints = array([1, 2, 3, 4, 5, 6, 7, 8])
for int1, int2 in ints.reshape(-1, 2):
    print(int1, int2)
