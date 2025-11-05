# Python3 code to demonstrate 
# converting list of strings to int 
# using map() 

# initializing list 
test_list = ['1', '4', '3', '6', '7'] 

# Printing original list 
print ("Original list is : " + str(test_list)) 

# using map() to 
# perform conversion 
test_list = list(map(int, test_list)) 
    

# Printing modified list 
print ("Modified list is : " + str(test_list)) 
