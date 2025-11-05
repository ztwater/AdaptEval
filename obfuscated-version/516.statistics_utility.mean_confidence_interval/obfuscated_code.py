import numpy as np
import scipy.stats

def mean_confidence_interval(var_0, var_1=0.95):
    var_2 = 1.0 * np.array(var_0)
    var_3 = len(var_2)
    m, se = np.mean(var_2), scipy.stats.sem(var_2)
    var_4 = se * scipy.stats.t.ppf((1 + var_1) / 2., var_3-1)
    return m, m-var_4, m+var_4
