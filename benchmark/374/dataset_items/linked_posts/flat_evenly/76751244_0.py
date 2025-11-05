from itertools import zip_longest

list_of_lists = [
    [1, 2, 3],
    [4, 5],
    [6, 8, 9, 10],
    [11]
    ]

flat_list = []
for tup in zip_longest(*list_of_lists, fillvalue=None):
    for e in tup:
        if e is not None:
            flat_list.append(e)

print(flat_list)
