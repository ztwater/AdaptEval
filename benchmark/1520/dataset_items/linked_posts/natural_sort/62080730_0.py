from typing import Tuple, Union, Optional, Generator


StrOrInt = Union[str, int]


# On Python 3.6, string concatenation is REALLY fast
# Tested myself, and this fella also tested:
# https://blog.ganssle.io/articles/2019/11/string-concat.html
def griter(s: str) -> Generator[StrOrInt, None, None]:
    last_was_digit: Optional[bool] = None
    cluster: str = ""
    for c in s:
        if last_was_digit is None:
            last_was_digit = c.isdigit()
            cluster += c
            continue
        if c.isdigit() != last_was_digit:
            if last_was_digit:
                yield int(cluster)
            else:
                yield cluster
            last_was_digit = c.isdigit()
            cluster = ""
        cluster += c
    if last_was_digit:
        yield int(cluster)
    else:
        yield cluster
    return


def grouper(s: str) -> Tuple[StrOrInt, ...]:
    return tuple(griter(s))
