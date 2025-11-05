def sizeof_fmt(num, use_kibibyte=True):
    base, suffix = [(1000.,'B'),(1024.,'iB')][use_kibibyte]
    for x in ['B'] + map(lambda x: x+suffix, list('kMGTP')):
        if -base < num < base:
            return "%3.1f %s" % (num, x)
        num /= base
    return "%3.1f %s" % (num, x)
