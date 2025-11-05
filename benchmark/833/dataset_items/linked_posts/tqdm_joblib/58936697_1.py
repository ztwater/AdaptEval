from math import sqrt
from joblib import Parallel, delayed

with tqdm_joblib(tqdm(desc="My calculation", total=10)) as progress_bar:
    Parallel(n_jobs=16)(delayed(sqrt)(i**2) for i in range(10))
