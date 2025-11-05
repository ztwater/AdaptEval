l1 = [1, 2, 3, 4, 5]
l2 = [1] * 5
l3 = []
all_equal = lambda l: len(l) > 0 and all(l[0] == e for e in l)
print(f"{all_equal(l1) = }")  # False
print(f"{all_equal(l2) = }")  # True
print(f"{all_equal(l3) = }")  # False

