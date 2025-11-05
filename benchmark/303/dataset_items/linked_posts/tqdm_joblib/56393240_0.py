from joblib import Parallel, delayed
from datetime import datetime
from tqdm import notebook

def myfun(x):
    return x**2

results = Parallel(n_jobs=8)(delayed(myfun)(i) for i in notebook.tqdm(range(1000)))  
