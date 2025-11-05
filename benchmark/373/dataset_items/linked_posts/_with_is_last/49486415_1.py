data_list = [1, 2, 3, 2, 1]
if data_list:
    while True:
        e = data_list.pop(0)
        if data_list:
            print(f'process element {e}')
        else:
            print(f'process last element {e}')
            break
else:
    print('list is empty')
