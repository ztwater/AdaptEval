split=lambda x,n: x if not x else [x[:n]]+[split([] if not -(len(x)-n) else x[-(len(x)-n):],n)][0]

split([1,2,3,4,5,6,7,8,9],2)

[[1, 2], [3, 4], [5, 6], [7, 8], [9]]
