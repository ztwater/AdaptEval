from typing import Sized, Iterable

def window(seq: Sized, n: int, strid: int = 1, drop_last: bool = False):
    for i in range(0, len(seq), strid):
        res = seq[i:i + n]
        if drop_last and len(res) < n:
            break
        yield res


def window2(seq: Iterable, n: int, strid: int = 1, drop_last: bool = False):
    it = iter(seq)
    result = []
    step = 0
    for i, ele in enumerate(it):
        result.append(ele)
        result = result[-n:]
        if len(result) == n:
            if step % strid == 0:
                yield result
            step += 1
    if not drop_last:
        yield result

