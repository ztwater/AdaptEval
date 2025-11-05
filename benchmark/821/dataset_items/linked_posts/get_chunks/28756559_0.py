l = [1,2,3,4,5,6,7,8,9,10,11,12]
k = 5 #chunk size
print [tuple(l[x:y]) for (x, y) in [(x, x+k) for x in range(0, len(l), k)]]
