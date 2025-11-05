from collections import OrderedDict
from functools import reduce
from itertools import groupby

import numpy as np
import pandas as pd
import perfplot
from more_itertools import unique_everseen as ue


def dict_fromkeys(data):
    return list(dict.fromkeys(data))


def unique_everseen(data):
    return list(ue(data))


def seen_add(data):
    seen = set()
    seen_add = seen.add
    return [x for x in data if not (x in seen or seen_add(x))]


def ordereddict_fromkeys(data):
    return list(OrderedDict.fromkeys(data))


def pandas_drop_duplicates(data):
    return pd.Series(data).drop_duplicates().tolist()


def pandas_unique(data):
    return pd.unique(data)


def itertools_groupby(data):
    return [key for key, _ in groupby(data)]


def reduce_tricks(data):
    return reduce(
        lambda r, v: v in r[1] and r or (r[0].append(v) or r[1].add(v)) or r,
        data,
        ([], set()),
    )[0]


b = perfplot.bench(
    setup=lambda n: np.random.randint(100, size=n).tolist(),
    kernels=[
        dict_fromkeys,
        unique_everseen,
        seen_add,
        ordereddict_fromkeys,
        pandas_drop_duplicates,
        pandas_unique,
        reduce_tricks,
    ],
    n_range=[2**k for k in range(20)],
)
b.save("out.png")
b.show()
