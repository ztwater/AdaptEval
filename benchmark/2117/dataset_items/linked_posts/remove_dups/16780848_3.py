list1 = ['b','c','d','b','c','a','a']    
list2 = []    
[list2.append(i) for i in list1 if not i in list2]    
print list2 
