data_list = [1, 2, 3, 2, 1]  # sample data
for i, e in enumerate(data_list):
    if i != len(data_list) - 1:
        print(f'process element {e}')
    else:
        print(f'process last element {e}')
