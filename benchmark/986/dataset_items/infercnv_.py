import re
from typing import Sequence
def _natural_sort(lst: Sequence):
    """Natural sort without third party libraries.
    Adapted from: https://stackoverflow.com/a/4836734/2340703
    """

    def convert(text):
        return int(text) if text.isdigit() else text.lower()

    def alphanum_key(key):
        return [convert(c) for c in re.split("([0-9]+)", key)]

    return sorted(lst, key=alphanum_key)
