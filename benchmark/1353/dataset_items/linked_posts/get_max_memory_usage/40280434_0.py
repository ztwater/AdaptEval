def get_proc_status(keys = None):
    with open('/proc/self/status') as f:
        data = dict(map(str.strip, line.split(':', 1)) for line in f)

    return tuple(data[k] for k in keys) if keys else data

peak, current = get_proc_status(('VmHWM', 'VmRSS'))
print(peak, current)  # outputs: 14280 kB 13696 kB
