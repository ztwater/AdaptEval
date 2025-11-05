import numpy as np
import pandas as pd
from numpy_ext import rolling_apply as rolling_apply_ext

def box_sum(a,b):
    return np.sum(a) + np.sum(b)

df = pd.DataFrame({"x": [1,2,3,4], "y": [1,2,3,4]})

window = 2
df["sum"] = rolling_apply_ext(box_sum, window , df.x.values, df.y.values)
