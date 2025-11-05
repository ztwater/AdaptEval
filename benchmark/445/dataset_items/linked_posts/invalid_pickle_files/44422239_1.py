 with open('test.pklz', 'rb') as ifp:
     print(pickle.load(ifp))
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
_pickle.UnpicklingError: invalid load key, ''.
