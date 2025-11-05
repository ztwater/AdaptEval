import time
def some_method(wait_time):
    time.sleep(wait_time)

with tqdm_joblib(tqdm(desc="My method", total=10)) as progress_bar:
    Parallel(n_jobs=2)(delayed(some_method)(0.2) for i in range(10))
