import numpy as np
df.iloc[:, np.setdiff1d(np.arange(len(df.columns)), unnecessary_cols)]
