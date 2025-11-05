 num = 65 # Input number
 array = np.random.random((10))*100 # Given array 
 nearest_idx = np.where(abs(array-num)==abs(array-num).min())[0] # If you want the index of the element of array (array) nearest to the the given number (num)
 nearest_val = array[abs(array-num)==abs(array-num).min()] # If you directly want the element of array (array) nearest to the given number (num)
