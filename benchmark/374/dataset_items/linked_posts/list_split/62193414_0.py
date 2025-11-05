my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list2 = [my_list[i:i+3] for i in range(0, len(my_list), 3)]
print(my_list2)
