num_list = [1, 2, 3, 4]

loop_count = len(num_list) - 1  # 3
for index, num in enumerate(num_list):
    if index == loop_count:
        print('this is the last iteration of the loop')
