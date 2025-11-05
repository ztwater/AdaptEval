In [95]: list(chunker(range(9),2) )                                                                                                                                          
Out[95]: [[0, 1], [2, 3], [4, 5], [6, 7], [8]]

In [96]: list(chunker([1,2,3,4,5],2) )                                                                                                                                       
Out[96]: [[1, 2], [3, 4], [5]]

In [97]: list(chunker(iter(range(9)),2) )                                                                                                                                    
Out[97]: [[0, 1], [2, 3], [4, 5], [6, 7], [8]]

In [98]: list(chunker(range(9),25) )                                                                                                                                         
Out[98]: [[0, 1, 2, 3, 4, 5, 6, 7, 8]]

In [99]: list(chunker(range(9),1) )                                                                                                                                          
Out[99]: [[0], [1], [2], [3], [4], [5], [6], [7], [8]]

In [101]: %timeit list(chunker(range(101),2) )                                                                                                                               
11.3 µs ± 68.2 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
