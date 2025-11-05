import numpy as np
from statsmodels.stats.weightstats import DescrStatsW

array = np.array([1,2,1,2,1,2,1,3])
weights = np.ones_like(array)
weights[3] = 100
