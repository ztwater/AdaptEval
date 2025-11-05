class BatchCompletionCallBack(object):
    # Added code - start
    global total_n_jobs
    # Added code - end
    def __init__(self, dispatch_timestamp, batch_size, parallel):
        self.dispatch_timestamp = dispatch_timestamp
        self.batch_size = batch_size
        self.parallel = parallel

    def __call__(self, out):
        self.parallel.n_completed_tasks += self.batch_size
        this_batch_duration = time.time() - self.dispatch_timestamp

        self.parallel._backend.batch_completed(self.batch_size,
                                           this_batch_duration)
        self.parallel.print_progress()
        # Added code - start
        progress = self.parallel.n_completed_tasks / total_n_jobs
        print(
            "\rProgress: [{0:50s}] {1:.1f}%".format('#' * int(progress * 50), progress*100)
            , end="", flush=True)
        if self.parallel.n_completed_tasks == total_n_jobs:
            print('\n')
        # Added code - end
        if self.parallel._original_iterator is not None:
            self.parallel.dispatch_next()

import joblib.parallel
import time
joblib.parallel.BatchCompletionCallBack = BatchCompletionCallBack
