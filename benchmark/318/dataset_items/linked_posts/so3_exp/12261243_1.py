>>> import timeit
>>> 
>>> setup = """
... import numpy as np
... import numpy.random as nr
... 
... from rotation_matrix_test import rotation_matrix_weave
... from rotation_matrix_test import rotation_matrix_numpy
... 
... mat1 = np.eye(3,3)
... theta = nr.random()
... axis = nr.random(3)
... """
>>> 
>>> timeit.repeat("rotation_matrix_weave(axis, theta, mat1)", setup=setup, number=100000)
[0.36641597747802734, 0.34883809089660645, 0.3459300994873047]
>>> timeit.repeat("rotation_matrix_numpy(axis, theta)", setup=setup, number=100000)
[7.180983066558838, 7.172032117843628, 7.180462837219238]
