# bytes pretty-printing
UNITS_MAPPING = [
    (1<<50, ' PB'),
    (1<<40, ' TB'),
    (1<<30, ' GB'),
    (1<<20, ' MB'),
    (1<<10, ' KB'),
    (1, (' byte', ' bytes')),
]


def pretty_size(bytes, units=UNITS_MAPPING):
    """Get human-readable file sizes.
    simplified version of https://pypi.python.org/pypi/hurry.filesize/
    """
    for factor, suffix in units:
        if bytes >= factor:
            break
    amount = int(bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix
        if amount == 1:
            suffix = singular
        else:
            suffix = multiple
    return str(amount) + suffix

print(pretty_size(1))
print(pretty_size(42))
print(pretty_size(4096))
print(pretty_size(238048577))
print(pretty_size(334073741824))
print(pretty_size(96995116277763))
print(pretty_size(3125899904842624))

## [Out] ###########################
1 byte
42 bytes
4 KB
227 MB
311 GB
88 TB
2 PB
