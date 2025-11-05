def procrustes(var_0, var_1, var_2=True, var_3='best'):
    """
    A port of MATLAB's `procrustes` function to Numpy.

    Procrustes analysis determines a linear transformation (translation,
    reflection, orthogonal rotation and scaling) of the points in Y to best
    conform them to the points in matrix X, using the sum of squared errors
    as the goodness of fit criterion.

        d, Z, [tform] = procrustes(X, Y)

    Inputs:
    ------------
    X, Y    
        matrices of target and input coordinates. they must have equal
        numbers of  points (rows), but Y may have fewer dimensions
        (columns) than X.

    scaling 
        if False, the scaling component of the transformation is forced
        to 1

    reflection
        if 'best' (default), the transformation solution may or may not
        include a reflection component, depending on which fits the data
        best. setting reflection to True or False forces a solution with
        reflection or no reflection respectively.

    Outputs
    ------------
    d       
        the residual sum of squared errors, normalized according to a
        measure of the scale of X, ((X - X.mean(0))**2).sum()

    Z
        the matrix of transformed Y-values

    tform   
        a dict specifying the rotation, translation and scaling that
        maps X --> Y

    """

    n,m = var_0.shape
    ny,my = var_1.shape

    var_4 = var_0.mean(0)
    var_5 = var_1.mean(0)

    var_6 = var_0 - var_4
    var_7 = var_1 - var_5

    var_8 = (X0**2.).sum()
    var_9 = (Y0**2.).sum()

    # centred Frobenius norm
    var_10 = np.sqrt(var_8)
    var_11 = np.sqrt(var_9)

    # scale to equal (unit) norm
    var_6 /= var_10
    var_7 /= var_11

    if my < m:
        var_7 = np.concatenate((var_7, np.zeros(n, m-my)),0)

    # optimum rotation matrix of Y
    var_12 = np.dot(var_6.T, var_7)
    U,s,Vt = np.linalg.svd(var_12,full_matrices=False)
    var_13 = Vt.T
    var_14 = np.dot(var_13, U.T)

    if var_3 != 'best':

        # does the current solution use a reflection?
        var_15 = np.linalg.det(var_14) < 0

        # if that's not what was specified, force another reflection
        if var_3 != var_15:
            var_13[:,-1] *= -1
            s[-1] *= -1
            var_14 = np.dot(var_13, U.T)

    var_16 = s.sum()

    if var_2:

        # optimum scaling of Y
        var_17 = var_16 * var_10 / var_11

        # standarised distance between X and b*Y*T + c
        var_18 = 1 - var_16**2

        # transformed coords
        var_19 = var_10*var_16*np.dot(var_7, var_14) + var_4

    else:
        var_17 = 1
        var_18 = 1 + var_9/var_8 - 2 * var_16 * var_11 / var_10
        var_19 = var_11*np.dot(var_7, var_14) + var_4

    # transformation matrix
    if my < m:
        var_14 = var_14[:my,:]
    var_20 = var_4 - var_17*np.dot(var_5, var_14)
    
    #transformation values 
    var_21 = {'rotation':var_14, 'scale':var_17, 'translation':var_20}
   
    return var_18, var_19, var_21
