data_list = [1, 2, 3, 2, 1]  # sample data
L = list(data_list)  # destroy L instead of data_list
while L:
    e = L.pop(0)
    if L:
        print(f'process element {e}')
    else:
        print(f'process last element {e}')
del L
