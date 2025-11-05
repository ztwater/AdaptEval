from pathlib import Path
from resource import getpagesize

PAGESIZE = getpagesize()
PATH = Path('/proc/self/statm')


def get_resident_set_size() -> int:
    """Return the current resident set size in bytes."""
    # statm columns are: size resident shared text lib data dt
    statm = PATH.read_text()
    fields = statm.split()
    return int(fields[1]) * PAGESIZE


data = []
start_memory = get_resident_set_size()
for _ in range(10):
    data.append('X' * 100000)
    print(get_resident_set_size() - start_memory)
