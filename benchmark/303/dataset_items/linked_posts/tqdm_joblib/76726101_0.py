from joblib import Parallel, delayed
from tqdm import tqdm

import time
import random

# Our example worker will sleep for a certain number of seconds.

inputs = list(range(10))
random.shuffle(inputs)

def worker(n_seconds):
    time.sleep(n_seconds)
    return n_seconds

# Run the worker jobs in parallel, with a tqdm progress bar.
# We configure Parallel to return a generator.
# Then we wrap the generator in tqdm.
# Finally, we execute everything by converting the tqdm generator to a list.

outputs = list(
    tqdm(
        # Note the new return_as argument here, which requires joblib >= 1.3:
        Parallel(return_as="generator", n_jobs=3)(
            delayed(worker)(n_seconds) for n_seconds in inputs
        ),
        total=len(inputs),
    )
)
print(outputs)
