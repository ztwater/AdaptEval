from joblib import Parallel, delayed
from datetime import datetime
from tqdm import tqdm

def myfun(x):
    return x**2

results = Parallel(n_jobs=8)(delayed(myfun)(i) for i in tqdm(range(1000))
100%|██████████| 1000/1000 [00:00<00:00, 10563.37it/s]
