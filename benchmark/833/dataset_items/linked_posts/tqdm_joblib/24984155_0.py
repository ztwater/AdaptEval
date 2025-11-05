# This is inside a dispatch function
self._lock.acquire()
job = self._pool.apply_async(SafeFunction(func), args,
            kwargs, callback=CallBack(self.n_dispatched, self))
self._jobs.append(job)
self.n_dispatched += 1
