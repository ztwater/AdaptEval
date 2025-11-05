def lis(l):

# we will create a list of lists where each sub-list contains
# the longest increasing subsequence ending at this index
lis = [[e] for e in l]
# start with just the elements of l as contents of the sub-lists

# iterate over (index,value) of l
for i, e in enumerate(l):
    # (index,value) tuples for elements b where b<e and a<i
    lower_tuples = filter(lambda (a,b): b<e, enumerate(l[:i]))
    # if no such items, nothing to do
    if not lower_tuples: continue
    # keep the lis-es of such items
    lowerlises = [lis[a] for a,b in  lower_tuples ]
    # choose the longest one of those and add
    # to the current element's lis
    lis[i] = max(lowerlises, key=len) + [e]

# retrun the longest of lis-es
return max(lis, key=len)
