n = len(lst)
# p is the number of parts to be divided
x = int(n/p)

i = 0
j = x
lstt = []
while (i< len(lst) or j <len(lst)):
    lstt.append(lst[i:j])
    i+=x
    j+=x
print(lstt)
