from IPython.display import *
from numpy import *
A = array([[12, 5, 2],
       [20, 4, 8],
       [ 2, 4, 3],
       [ 7, 1,10]])

latexA = '$$\n' + r'\begin{bmatrix}' + '\n' + (r'\\' + '\n').join('&'.join(str(x) for x in row) for row in A) + '\n' + r'\end{bmatrix}' + '\n' +'$$'
print(latexA)

display(Latex(latexA))
