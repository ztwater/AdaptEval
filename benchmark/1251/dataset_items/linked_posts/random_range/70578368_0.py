import random

LENGTH = 100

random_with_possible_duplicates = [random.randrange(-3, 3) for _ in range(LENGTH)]
random_without_duplicates = list(set(random_with_possible_duplicates)) # This removes duplicates
