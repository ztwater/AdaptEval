from itertools import repeat


xs = list(range(1, 9))  # [1, 2, 3, 4, 5, 6, 7, 8]
xs_pow_2 = list(map(pow, xs, repeat(2)))  # [1, 4, 9, 16, 25, 36, 49, 64]
