# Python3 code to demonstrate 
# converting list of strings to int 
# using list comprehension 

# initializing list 
test_list = ['1', '4', '3', '6', '7'] 

# Printing original list 
print ("Original list is : " + str(test_list)) 

# using list comprehension to 
# perform conversion 
test_list = [int(i) for i in test_list] 
    

# Printing modified list 
print ("Modified list is : " + str(test_list)) 
