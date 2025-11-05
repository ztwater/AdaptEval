import os
workers = os.cpu_count()
if 'sched_getaffinity' in dir(os):
    workers = len(os.sched_getaffinity(0))
