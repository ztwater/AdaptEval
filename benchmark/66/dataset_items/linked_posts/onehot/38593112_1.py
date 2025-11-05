import numpy as np

def one_hot(i):
    a = np.zeros(10, 'uint8')
    a[i] = 1
    return a

a = one_hot(5) 
print(a)
