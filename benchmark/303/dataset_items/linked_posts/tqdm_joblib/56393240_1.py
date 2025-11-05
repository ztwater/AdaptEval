from joblib import Parallel, delayed
from datetime import datetime
from tqdm import notebook
from random import randint
import time

def myfun(x):
    time.sleep(randint(1, 5))
    return x**2

results = Parallel(n_jobs=7)(delayed(myfun)(i) for i in notebook.tqdm(range(100)))
