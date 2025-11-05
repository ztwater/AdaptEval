def split_list(the_list, chunk_size):
    result_list = []
    while the_list:
        result_list.append(the_list[:chunk_size])
        the_list = the_list[chunk_size:]
    return result_list

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print split_list(a_list, 3)
