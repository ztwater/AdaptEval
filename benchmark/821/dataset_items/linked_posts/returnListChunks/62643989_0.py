l = [1,2,3,4,5,6,7,8,9]
n = 3
outList = []
for i in range(n, len(l) + n, n):
    outList.append(l[i-n:i])

print(outList)
