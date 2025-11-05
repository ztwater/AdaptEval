import math
def find_median(arr):
    if len(arr)%2==1:
        med=math.ceil(len(arr)/2)-1
        return arr[med]
    else:
        return -1
print(find_median([1,2,3,4,5,6,7,8]))
