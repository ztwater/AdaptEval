import re
from itertools import cycle

_re_digits = re.compile(r"(\d+)")


def natural_comparison_key(key):
    return tuple(
        int(part) if is_digit else part
        for part, is_digit in zip(_re_digits.split(key), cycle((False, True)))
    )
