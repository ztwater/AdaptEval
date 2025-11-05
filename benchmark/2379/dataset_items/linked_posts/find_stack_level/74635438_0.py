import sys
from collections import namedtuple


FrameInfo = namedtuple('FrameInfo', ['filename', 'lineno', 'function'])


def frame_info(walkback=0):
    # NOTE: sys._getframe() is a tiny bit faster than inspect.currentframe()
    #   Although the function name is prefixed with an underscore, it is
    #   documented and fine to use assuming we are running under CPython:
    #
    #   https://docs.python.org/3/library/sys.html#sys._getframe
    #
    frame = sys._getframe().f_back

    for __ in range(walkback):
        f_back = frame.f_back
        if not f_back:
            break

        frame = f_back

    return FrameInfo(frame.f_code.co_filename, frame.f_lineno, frame.f_code.co_name)
