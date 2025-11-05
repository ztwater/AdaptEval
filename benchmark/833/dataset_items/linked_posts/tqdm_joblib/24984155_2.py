def print_progress(self, index):
    elapsed_time = time.time() - self._start_time

    # This is heuristic code to print only 'verbose' times a messages
    # The challenge is that we may not know the queue length
    if self._original_iterable:
        if _verbosity_filter(index, self.verbose):
            return
        self._print('Done %3i jobs       | elapsed: %s',
                    (index + 1,
                     short_format_time(elapsed_time),
                    ))
    else:
        # We are finished dispatching
        queue_length = self.n_dispatched
        # We always display the first loop
        if not index == 0:
            # Display depending on the number of remaining items
            # A message as soon as we finish dispatching, cursor is 0
            cursor = (queue_length - index + 1
                      - self._pre_dispatch_amount)
            frequency = (queue_length // self.verbose) + 1
            is_last_item = (index + 1 == queue_length)
            if (is_last_item or cursor % frequency):
                return
        remaining_time = (elapsed_time / (index + 1) *
                    (self.n_dispatched - index - 1.))
        self._print('Done %3i out of %3i | elapsed: %s remaining: %s',
                    (index + 1,
                     queue_length,
                     short_format_time(elapsed_time),
                     short_format_time(remaining_time),
                    ))
