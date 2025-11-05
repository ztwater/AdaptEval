class CallBack(object):
    """ Callback used by parallel: it is used for progress reporting, and
        to add data to be processed
    """
    def __init__(self, index, parallel):
        self.parallel = parallel
        self.index = index

    def __call__(self, out):
        self.parallel.print_progress(self.index)
        if self.parallel._original_iterable:
            self.parallel.dispatch_next()
