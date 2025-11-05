[key1 == key2 and dict1.get(key1).update(dict2.get(key2)) 
 for key1, key2 in zip(dict1, dict2)]
print dict1
