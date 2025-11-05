import numpy as np

x = np.random.random((5000, 5000)) - 0.5
print("max method:")
%timeit -n10 np.maximum(x, 0)

print("multiplication method:")
%timeit -n10 x * (x > 0)

print("abs method:")
%timeit -n10 (abs(x) + x) / 2
