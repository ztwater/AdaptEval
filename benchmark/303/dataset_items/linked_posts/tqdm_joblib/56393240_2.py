import concurrent.futures
from tqdm import notebook
from random import randint
import time

iterable = [i for i in range(50)]

def myfun(x):
    time.sleep(randint(1, 5))
    return x**2

def run(func, iterable, max_workers=8):
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(notebook.tqdm(executor.map(func, iterable), total=len(iterable)))
    return results

run(myfun, iterable)
