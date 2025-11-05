def longest_sub_seq(arr):
    main_arr = []
    sub_arr = []
    n = len(arr)
    for ind in range(n):
        if ind < n - 1 and arr[ind] <= arr[ind+1]:
           sub_arr.append(arr[ind])
        else:
           sub_arr.append(arr[ind])
           main_arr.append(sub_arr)
           sub_arr = []
    return max(main_arr, key=len)

a = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12, 1, 2, 3]
print(longest_sub_seq(a)) # op: [4, 5, 6, 7, 8, 12]
