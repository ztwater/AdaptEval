l1 = [1, 2, 3, 4, 1, 2, 3, 4, 5]
l2 = [x for x in l1 if x not in locals()['_[1]']]
print l2
