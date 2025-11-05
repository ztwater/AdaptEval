def PdistIndices(n,I):
    '''idx = {} indices for pdist results'''
    idx = numpy.array(numpy.triu_indices(n,1)).T[I]
    return idx
