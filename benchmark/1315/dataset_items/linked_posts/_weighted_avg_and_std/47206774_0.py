import pandas as pd
import numpy as np
# X is the dataset, as a Pandas' DataFrame
# Compute the weighted sample mean (fast, efficient and precise)
mean = np.ma.average(X, axis=0, weights=weights) 

# Convert to a Pandas' Series (it's just aesthetic and more 
# ergonomic; no difference in computed values)
mean = pd.Series(mean, index=list(X.keys())) 
xm = X-mean # xm = X diff to mean
# fill NaN with 0 
# a variance of 0 is just void, but at least it keeps the other
# covariance's values computed correctly))
xm = xm.fillna(0) 
# Compute the unbiased weighted sample covariance
sigma2 = 1./(w.sum()-1) * xm.mul(w, axis=0).T.dot(xm); 
