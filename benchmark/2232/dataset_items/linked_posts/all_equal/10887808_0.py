def compare_lists(list1, list2):
    if len(list1) != len(list2): # Weed out unequal length lists.
        return False
    for item in list1:
        if item not in list2:
            return False
    return True

a_list_1 = ['apple', 'orange', 'grape', 'pear']
a_list_2 = ['pear', 'orange', 'grape', 'apple']

b_list_1 = ['apple', 'orange', 'grape', 'pear']
b_list_2 = ['apple', 'orange', 'banana', 'pear']

c_list_1 = ['apple', 'orange', 'grape']
c_list_2 = ['grape', 'orange']

print compare_lists(a_list_1, a_list_2) # Returns True
print compare_lists(b_list_1, b_list_2) # Returns False
print compare_lists(c_list_1, c_list_2) # Returns False
