import sys
from itertools import count

depth_offset = 9

def stack_size(size=2):
    """
    Get stack size for caller's frame, i.e. how many functions deep we are.
    Used to nest log messages from inner calls.
    https://stackoverflow.com/a/47956089
    """
    try:
        frame = sys._getframe(size)
        for size in count(size):
            frame = frame.f_back
            if not frame:
                return size
    except ValueError:
        # fallback
        return depth_offset
