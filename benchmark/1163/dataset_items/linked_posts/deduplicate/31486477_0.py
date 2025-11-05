    import pandas as pd
    import numpy as np

    uniquifier = lambda alist: pd.Series(alist).drop_duplicates().tolist()

    # from the chosen answer 
    def f7(seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if not (x in seen or seen_add(x))]

    alist = np.random.randint(low=0, high=1000, size=10000).tolist()

    print uniquifier(alist) == f7(alist)  # True
