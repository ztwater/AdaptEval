import numpy as np
import pandas as pd
from numpy_ext import rolling_apply


def masscenter(price, nQty):
    return np.sum(price * nQty) / np.sum(nQty)


df = pd.DataFrame( [['02:59:47.000282', 87.60, 739],
                    ['03:00:01.042391', 87.51, 10],
                    ['03:00:01.630182', 87.51, 10],
                    ['03:00:01.635150', 88.00, 792],
                    ['03:00:01.914104', 88.00, 10]], 
                   columns=['stamp', 'price','nQty'])
df['stamp'] = pd.to_datetime(df['stamp'], format='%H:%M:%S.%f')
df.set_index('stamp', inplace=True, drop=True)

window = 2
df['y'] = rolling_apply(masscenter, window, df.price.values, df.nQty.values)
print(df)

                            price  nQty          y
stamp                                             
1900-01-01 02:59:47.000282  87.60   739        NaN
1900-01-01 03:00:01.042391  87.51    10  87.598798
1900-01-01 03:00:01.630182  87.51    10  87.510000
1900-01-01 03:00:01.635150  88.00   792  87.993890
1900-01-01 03:00:01.914104  88.00    10  88.000000
