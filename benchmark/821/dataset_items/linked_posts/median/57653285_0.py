import numpy as np
def get_median(xs):
        mid = len(xs) // 2  # Take the mid of the list
        if len(xs) % 2 == 1: # check if the len of list is odd
            return sorted(xs)[mid] #if true then mid will be median after sorting
        else:
            #return 0.5 * sum(sorted(xs)[mid - 1:mid + 1])
            return 0.5 * np.sum(sorted(xs)[mid - 1:mid + 1]) #if false take the avg of mid
print(get_median([7, 7, 3, 1, 4, 5]))
print(get_median([1,2,3, 4,5]))
