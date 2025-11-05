import numpy as np

def array_to_bmatrix(array):
    array = np.atleast_2d(array)
    begin = '\\begin{bmatrix} \n'
    data = ''
    for line in array:
