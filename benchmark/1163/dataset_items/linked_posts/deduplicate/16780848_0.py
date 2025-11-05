list1 = ['b','c','d','b','c','a','a']    
list2 = list(set(list1))    
list2.sort(key=list1.index)    
print list2
