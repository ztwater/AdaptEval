import math

# length of the list len(lst) is ln
# size of a chunk is size

for num in range ( math.ceil(ln/size) ):
    start, end = num*size, min((num+1)*size, ln)
    print(lst[start:end])
