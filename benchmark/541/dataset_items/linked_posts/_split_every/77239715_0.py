from itertools import batched
batched("ABCDEFG", 2)  # --> (("A", "B"), ("C", "D"), ("E",))
batched(range(8), 3)  # --> ((1, 2, 3), (4, 5, 6), (7, 8))
