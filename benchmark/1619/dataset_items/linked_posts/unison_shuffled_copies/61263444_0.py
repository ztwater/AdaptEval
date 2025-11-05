import numpy as np
def shuffle_in_unison(a,b):

    assert len(a)==len(b)
    c = np.arange(len(a))
    np.random.shuffle(c)

    return a[c],b[c]

a =  np.asarray([[1, 1], [2, 2], [3, 3]])
b =  np.asarray([11, 22, 33])

shuffle_in_unison(a,b)
Out[94]: 
(array([[3, 3],
        [2, 2],
        [1, 1]]),
 array([33, 22, 11]))
