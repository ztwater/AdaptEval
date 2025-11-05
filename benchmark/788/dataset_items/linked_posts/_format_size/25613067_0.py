from math import log2

_suffixes = ['bytes', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']

def file_size(size):
    # Determine binary order in steps of size 10
    # (coerce to int, // still returns a float)
    order = int(log2(size) / 10) if size else 0

    # Format file size
    # (.4g results in rounded numbers for exact matches
    # and maximum 3 decimals, and should never resort
    # to exponent values)
    return '{:.4g} {}'.format(size / (1 << (order * 10)), _suffixes[order])
