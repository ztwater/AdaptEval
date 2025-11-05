l = [1,2,2,3,3,...]
n = []
n.extend(ele for ele in l if ele not in set(n))
