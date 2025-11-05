b = np.array([1,3,3, 8, 12, 12,12])    
numpy.hstack([b[0], [x[0] for x in zip(b[1:], b[:-1]) if x[0]!=x[1]]])
