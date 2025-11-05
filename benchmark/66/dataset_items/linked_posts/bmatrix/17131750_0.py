import numpy as np

def bmatrix(a):
    """Returns a LaTeX bmatrix

    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']
    return '\n'.join(rv)

A = np.array([[12, 5, 2], [20, 4, 8], [ 2, 4, 3], [ 7, 1, 10]])
print bmatrix(A) + '\n'

B = np.array([[1.2], [3.7], [0.2]])
print bmatrix(B) + '\n'

C = np.array([1.2, 9.3, 0.6, -2.1])
print bmatrix(C) + '\n'
