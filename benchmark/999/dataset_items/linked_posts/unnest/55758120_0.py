def stack(df):
    return df.set_index(['A', 'C']).B.apply(pd.Series).stack()


def comprehension(df):
    return pd.DataFrame([x + [z] for x, y in zip(df[['A', 'C']].values.tolist(), df.B) for z in y])


def multiindex(df):
    return pd.DataFrame(np.concatenate(df.B.values), index=df.set_index(['A', 'C']).index.repeat(df.B.str.len()))


def array(df):
    return pd.DataFrame(
        np.column_stack((
            np.repeat(df[['A', 'C']].values, df.B.str.len(), axis=0),
            np.concatenate(df.B.values)
        ))
    )


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from timeit import timeit

res = pd.DataFrame(
    index=[
        'stack',
        'comprehension',
        'multiindex',
        'array',
    ],
    columns=[1000, 2000, 5000, 10000, 20000, 50000],
    dtype=float
)

for f in res.index:
    for c in res.columns:
        df = pd.DataFrame({'A': list('abc'), 'C': list('def'), 'B': [['g', 'h', 'i'], ['j', 'k'], ['l']]})
        df = pd.concat([df] * c)
        stmt = '{}(df)'.format(f)
        setp = 'from __main__ import df, {}'.format(f)
        res.at[f, c] = timeit(stmt, setp, number=20)

ax = res.div(res.min()).T.plot(loglog=True)
ax.set_xlabel("N")
ax.set_ylabel("time (relative)")
