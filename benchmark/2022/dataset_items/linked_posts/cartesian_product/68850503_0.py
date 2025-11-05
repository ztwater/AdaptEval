>>>x1, y1 = np.meshgrid(x, y)
>>>np.c_[x1.ravel(), y1.ravel()]
array([[1, 4],
       [2, 4],
       [3, 4],
       [1, 5],
       [2, 5],
       [3, 5]])
