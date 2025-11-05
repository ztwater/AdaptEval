some_list = list(range(0, 20))  # creates a list of 20 elements
generator = comb(some_list, 4)  # creates a generator that will generate lists of 4 elements
for sublist in generator:
    print(sublist)  # prints a sublist of four elements, as it's generated
