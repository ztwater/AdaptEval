def PolyArea(var_0,var_1):
    return 0.5*np.abs(np.dot(var_0,np.roll(var_1,1))-np.dot(var_1,np.roll(var_0,1)))
