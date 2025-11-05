import pandas as pd
import numpy as np
from numba import jit

df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6], 'b': [1, 3, 5, 7, 9, 11]})

@jit
def f(w):
    # we have access to both columns of the dataframe here
    return np.max(w), np.min(w)

df.rolling(3, method='table').apply(f, raw=True, engine='numba')
