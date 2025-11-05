rle([True, True, True, False, True, False, False])
Out[8]: 
(array([3, 1, 1, 2]),
 array([0, 3, 4, 5]),
 array([ True, False,  True, False], dtype=bool))

rle(np.array([5, 4, 4, 4, 4, 0, 0]))
Out[9]: (array([1, 4, 2]), array([0, 1, 5]), array([5, 4, 0]))

rle(["hello", "hello", "my", "friend", "okay", "okay", "bye"])
Out[10]: 
(array([2, 1, 1, 2, 1]),
 array([0, 2, 3, 4, 6]),
 array(['hello', 'my', 'friend', 'okay', 'bye'], 
       dtype='|S6'))
