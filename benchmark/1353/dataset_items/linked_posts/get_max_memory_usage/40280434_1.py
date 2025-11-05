import resource


def report():
    maxrss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak, current = get_proc_status(('VmHWM', 'VmRSS'))
    print(current, peak, maxrss)


report()

s = ' ' * 2 ** 28  # 256MiB
report()

s = None
report()
