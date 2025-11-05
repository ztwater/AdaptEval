from itertools import zip_longest, product

def xplode(df, explode, zipped=True):
    method = zip_longest if zipped else product

    rest = {*df} - {*explode}

    zipped = zip(zip(*map(df.get, rest)), zip(*map(df.get, explode)))
    tups = [tup + exploded
     for tup, pre in zipped
     for exploded in method(*pre)]

    return pd.DataFrame(tups, columns=[*rest, *explode])[[*df]]
