>>> from scipy.sparse import csr_matrix
>>> A = csr_matrix([[0,0,2,0], [0,1,0,3]])
>>> print(A)
  (0, 2)    2
  (1, 1)    1
  (1, 3)    3
>>> B = A.reshape((4,2))
>>> print(B)
  (1, 0)    2
  (2, 1)    1
  (3, 1)    3
>>> C = A.reshape((4,2), order='F')
>>> print(C)
  (0, 1)    2
  (3, 0)    1
  (3, 1)    3

