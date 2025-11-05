import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from timeit import timeit

res = pd.DataFrame(
       index=['wen1', 'wen2', 'wen3', 'wen4', 'chris1', 'chris2'],
       columns=[10, 50, 100, 500, 1000, 5000, 10000],
       dtype=float
)

for f in res.index:
    for c in res.columns:
        df = pd.DataFrame({'A': [1, 2], 'B': [[1, 2], [1, 2]]})
        df = pd.concat([df]*c)
        stmt = '{}(df)'.format(f)
        setp = 'from __main__ import df, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=50)

ax = res.div(res.min()).T.plot(loglog=True)
ax.set_xlabel("N")
ax.set_ylabel("time (relative)")
