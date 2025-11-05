x = [1, 2, 1, 3, 1, 4]

# brute force method
arr = []
for i in x:
  if not i in arr:
    arr.insert(x[i],i)

# recursive method
tmp = []
def remove_duplicates(j=0):
    if j < len(x):
      if not x[j] in tmp:
        tmp.append(x[j])
      i = j+1  
      remove_duplicates(i)

      

remove_duplicates()
