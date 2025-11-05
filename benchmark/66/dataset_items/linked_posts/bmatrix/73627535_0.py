import numpy as np
import sympy as sym
from IPython.display import display, Math
A = np.array([[12, 5, 2],
       [20, 4, 8],
       [ 2, 4, 3],
       [ 7, 1,10]])
A = sym.Matrix(A)
display(A)
