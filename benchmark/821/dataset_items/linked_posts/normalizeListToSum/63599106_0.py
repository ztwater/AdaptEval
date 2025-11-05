from sklearn.preprocessing import normalize

x = [1,2,3,4]
normalize([x]) # array([[0.18257419, 0.36514837, 0.54772256, 0.73029674]])
normalize([x], norm="l1") # array([[0.1, 0.2, 0.3, 0.4]])
normalize([x], norm="max") # array([[0.25, 0.5 , 0.75, 1.]])
