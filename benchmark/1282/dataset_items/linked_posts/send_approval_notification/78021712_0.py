# Original: wrong
f_list = [
    (lambda x: x + i) for i in range(10)
]
print([f(3) for f in f_list])

# Correct, but not so intuitive
f_list = [
    (lambda x, i=i: x + i) for i in range(10)
]
print([f(3) for f in f_list])

# More intuitive, but not so readable
f_list = [
    (lambda i: (lambda x: x + i))(i) for i in range(10)
]
print([f(3) for f in f_list])

# More readable
get_f = lambda i: (lambda x: x + i)
f_list = [
    get_f(i) for i in range(10)
]
print([f(3) for f in f_list])
