myList = list(range(18))  # given list
N = 5  # desired number of parts

[myList[(i*len(myList))//N:((i+1)*len(myList))//N] for i in range(N)]
# [[0, 1, 2], [3, 4, 5, 6], [7, 8, 9], [10, 11, 12, 13], [14, 15, 16, 17]]
