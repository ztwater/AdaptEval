def my_cubic_interp1d(x0, x, y):
    """
    Interpolate a 1-D function using cubic splines.
      x0 : a 1d-array of floats to interpolate at
      x : a 1-D array of floats sorted in increasing order
      y : A 1-D array of floats. The length of y along the
          interpolation axis must be equal to the length of x.

    Implement a trick to generate at first step the cholesky matrice L of
    the tridiagonal matrice A (thus L is a bidiagonal matrice that
    can be solved in two distinct loops).

    additional ref: www.math.uh.edu/~jingqiu/math4364/spline.pdf 
    # original function code at: https://stackoverflow.com/a/48085583/36061
    
    
    This function is licenced under: Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)
    https://creativecommons.org/licenses/by-sa/3.0/
    Original Author raphael valentin
    Date 3 Jan 2018
    
    
    Modifications made to remove numpy dependencies:
        -all sub-functions by MR
        
    This function, and all sub-functions, are licenced under: Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)        
        
    Mod author: Matthew Rowles
    Date 3 May 2021
    
    """
    def diff(lst):
        """
        numpy.diff with default settings
        """
        size = len(lst)-1
        r = [0]*size
        for i in range(size):
            r[i] = lst[i+1] - lst[i] 
        return r
    
    def list_searchsorted(listToInsert, insertInto):
        """
        numpy.searchsorted with default settings
        """
        def float_searchsorted(floatToInsert, insertInto):
            for i in range(len(insertInto)):
                if floatToInsert <= insertInto[i]:
                    return i
            return len(insertInto)
        return [float_searchsorted(i, insertInto) for i in listToInsert]
    
    def clip(lst, min_val, max_val, inPlace = False):    
        """
        numpy.clip
        """
        if not inPlace:
            lst = lst[:]  
        for i in range(len(lst)):
            if lst[i] < min_val:
                lst[i] = min_val
            elif lst[i] > max_val:
                lst[i] = max_val  
        return lst
    
    def subtract(a,b):
        """
        returns a - b
        """
        return a - b
    
    size = len(x)

    xdiff = diff(x)
    ydiff = diff(y)

    # allocate buffer matrices
    Li   = [0]*size
    Li_1 = [0]*(size-1)
    z    = [0]*(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0]   = sqrt(2*xdiff[0])
    Li_1[0] = 0.0
    B0      = 0.0 # natural boundary
    z[0]    = B0 / Li[0]

    for i in range(1, size-1, 1):
        Li_1[i] = xdiff[i-1] / Li[i-1]
        Li[i] = sqrt(2*(xdiff[i-1]+xdiff[i]) - Li_1[i-1] * Li_1[i-1])
        Bi = 6*(ydiff[i]/xdiff[i] - ydiff[i-1]/xdiff[i-1])
        z[i] = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    i = size - 1
    Li_1[i-1] = xdiff[-1] / Li[i-1]
    Li[i]     = sqrt(2*xdiff[-1] - Li_1[i-1] * Li_1[i-1])
    Bi        = 0.0 # natural boundary
    z[i]      = (Bi - Li_1[i-1]*z[i-1])/Li[i]

    # solve [L.T][x] = [y]
    i = size-1
    z[i] = z[i] / Li[i]
    for i in range(size-2, -1, -1):
        z[i] = (z[i] - Li_1[i-1]*z[i+1])/Li[i]

    # find index
    index = list_searchsorted(x0,x)
    index = clip(index, 1, size-1)

    xi1 = [x[num]   for num in index]
    xi0 = [x[num-1] for num in index]
    yi1 = [y[num]   for num in index]
    yi0 = [y[num-1] for num in index]
    zi1 = [z[num]   for num in index]
    zi0 = [z[num-1] for num in index]
    hi1 = list( map(subtract, xi1, xi0) )

    # calculate cubic - all element-wise multiplication
    f0 = [0]*len(hi1)
    for j in range(len(f0)):
        f0[j] = zi0[j]/(6*hi1[j])*(xi1[j]-x0[j])**3 + \
                zi1[j]/(6*hi1[j])*(x0[j]-xi0[j])**3 + \
                (yi1[j]/hi1[j] - zi1[j]*hi1[j]/6)*(x0[j]-xi0[j]) + \
                (yi0[j]/hi1[j] - zi0[j]*hi1[j]/6)*(xi1[j]-x0[j])        
    
    return f0
