functions = []
for i in range(3): 
    functions.append(lambda i=i: i)
print([f() for f in functions])
# [0, 1, 2]
