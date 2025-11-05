import contextlib
import joblib
from tqdm import tqdm

@contextlib.contextmanager
def tqdm_joblib(var_0):
    """Context manager to patch joblib to report into tqdm progress bar given as argument"""
    class TqdmBatchCompletionCallback(joblib.parallel.BatchCompletionCallBack):
        def __call__(self, *var_1, **var_2):
            var_0.update(n=self.batch_size)
            return super().__call__(*var_1, **var_2)

    var_3 = joblib.parallel.BatchCompletionCallBack
    joblib.parallel.BatchCompletionCallBack = TqdmBatchCompletionCallback
    try:
        yield var_0
    finally:
        joblib.parallel.BatchCompletionCallBack = var_3
        var_0.close()
