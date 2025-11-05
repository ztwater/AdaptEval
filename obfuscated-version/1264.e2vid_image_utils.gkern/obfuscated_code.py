import numpy as np
import scipy.stats as st

def gkern(var_0=21, var_1=3):
    """Returns a 2D Gaussian kernel array."""

    var_2 = (2*var_1+1.)/(var_0)
    var_3 = np.linspace(-var_1-var_2/2., var_1+var_2/2., var_0+1)
    var_4 = np.diff(st.norm.cdf(var_3))
    var_5 = np.sqrt(np.outer(var_4, var_4))
    var_6 = var_5/var_5.sum()
    return var_6
